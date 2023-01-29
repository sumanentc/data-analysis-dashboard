import pandas as pd
import numpy as np
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function to calculate the order value variability for a given year and quarter
def order_value_variability(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the order value variability for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the order value variability for
    :param quarter: The quarter to calculate the order value variability for
    :return: The order value variability for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Group data by order number and calculate the order total
    total_order = data.groupby('InvoiceNo')['TotalPrice'].sum()

    # Calculate the order value variability
    return round(np.std(total_order),2)
