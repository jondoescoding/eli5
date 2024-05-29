import pandas as pd

def extract_csv_data(path_to_data: str) -> pd.core.frame.DataFrame:
    """
    Extracts data from a CSV file located at the specified `path_to_data` and prints the first row of the filtered data.

    Args:
        path_to_data (str): The path to the CSV file.

    Returns:
        pd.core.frame.DataFrame: The first row of the filtered data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV file cannot be parsed.

    """
    # Load the TYC dataset
    # The data is a pandas DataFrame object
    data = pd.read_csv(filepath_or_buffer=path_to_data)
    
    # Filter the data to get only the rows where the 'DONE' column is null
    # The filtered data is a pandas DataFrame object
    filtered_data = data.loc[data['DONE'] == 0]
    
    # Return the first row of the filtered data
    return filtered_data.iloc[0].to_dict()
