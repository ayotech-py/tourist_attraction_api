import pandas as pd

def filter_csv_string(input_list):
    # read the CSV file
    df = pd.read_csv('browser_history.csv')
    
    # extract the column containing the string to be filtered
    string_col = df['history_string']
    
    # filter out rows containing elements from the given list
    filtered_df = df[~string_col.str.contains('|'.join(input_list))]
    
    # return the filtered dataframe
    return filtered_df
