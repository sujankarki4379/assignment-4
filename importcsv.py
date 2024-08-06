import csv
from statistics import mean

def read_csv(file_path):
    """
    Reads the content of a CSV file located at file_path.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV data.
        list: A list of column names from the CSV file.
    """
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data, reader.fieldnames
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except csv.Error as e:
        print(f"CSV error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None, None

def process_data(data, column_name):
    """
    Calculates the average of the values in the specified column and adds a new column with the average to each row.

    Args:
        data (list): The list of dictionaries representing the CSV data.
        column_name (str): The name of the column to calculate the average for.

    Returns:
        list: The processed data with an added 'average' column.
    """
    try:
        values = [float(row[column_name]) for row in data]
        avg = mean(values)
        for row in data:
            row['average'] = avg
        return data
    except KeyError:
        print(f"Error: The column {column_name} does not exist in the data.")
    except ValueError:
        print(f"Error: The column {column_name} contains non-numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def write_csv(file_path, data):
    """
    Writes the processed data to a new CSV file located at file_path.

    Args:
        file_path (str): The path to the new CSV file.
        data (list): The processed data to be written to the CSV file.
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
    except PermissionError:
        print(f"Error: Permission denied for writing to {file_path}.")
    except csv.Error as e:
        print(f"CSV error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file_path = 'input.csv'
    output_file_path = 'output.csv'
    column_name_to_average = 'score'

    data, columns = read_csv(input_file_path)
    if data:
        processed_data = process_data(data, column_name_to_average)
        if processed_data:
            write_csv(output_file_path, processed_data)
            print("Data written successfully to output.csv")
