import pandas as pd

# Write a function to filter a pandas dataframe by year and quarter
def filter_by_year_and_quarter(df, year, quarter):

    # Filter the dataframe by the year and quarter
    filtered_df = df[(df['Year'] == year) & (df['Quarter'] == quarter)]

    # Return the filtered dataframe
    if filtered_df.shape[0] > 0:
        return filtered_df
    else:
        assert filtered_df.shape[0] > 0, "There are no records for the specified year and quarter"
