import pandas as pd

tourist_types = ['Adventure tourists', 'Cultural tourists', 'Beach tourists', 'Eco-tourists', 'Wildlife tourists', 'Food tourists', 'Luxury tourists', 'Budget tourists', 'Educational tourists', 'Medical tourists', 'Religious tourists', 'Backpackers', 'Business tourists', 'Sports tourists', 'Music tourists', 'Art tourists', 'Sustainable tourists', 'Heritage tourists', 'Nature tourists', 'Road trippers', 'Cruise tourists', 'Family tourists', 'Group tourists', 'Solo tourists', 'Honeymooners', 'Winter sports tourists', 'Spa and wellness tourists', 'Urban tourists', 'Rural tourists', 'Volunteer tourists', 'Festival tourists', 'Film tourism', 'Historical tourists', 'Archaeological tourists', 'Geotourists', 'Garden tourists', 'Shopping tourists', 'Artisan tourists', 'Beer tourists', 'LGBT tourists', 'Motorcycle tourists', 'Train tourists', 'Plane spotters', 'War history tourists', 'Space tourists', 'Dark tourism', 'Backpacking couples', 'Digital nomads', 'Glamping tourists', 'Sightseeing tourists']


def filter_csv_string(input_list):
    # read the CSV file
    df = pd.read_csv('browser_history.csv')
    
    # extract the column containing the string to be filtered
    string_col = df['history_string']
    
    # filter out rows containing elements from the given list
    filtered_df = df[~string_col.str.contains('|'.join(input_list))]
    
    # return the filtered dataframe
    return filtered_df
