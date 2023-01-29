import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function to calculate mean number of customers per day
def mean_customers_per_day(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the mean number of customers per day for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the mean number of customers per day for
    :param quarter: The quarter to calculate the mean number of customers per day for
    :return: The mean number of customers per day for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Calculate the mean number of customers per day
    return round(data.groupby(['Month', 'Day']).nunique()['CustomerID'].mean(), 2)
