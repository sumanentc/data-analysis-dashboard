import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

def total_sales(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the total sales for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the total sales for
    :param quarter: The quarter to calculate the total sales for
    :return: The total sales for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Calculate the total sales
    return round(data['TotalPrice'].sum(),2)
    
