import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

def customer_retention_rate(data: pd.DataFrame, year: int, quarter: int) -> float:
    """
    Calculate the customer retention rate for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to calculate the customer retention rate for
    :param quarter: The quarter to calculate the customer retention rate for
    :return: The customer retention rate for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Calculate the number of unique customers
    num_customers = data['CustomerID'].nunique()

    # Calculate the number of repeat customers
    num_repeat_customers = sum(data.groupby(['CustomerID']).count()['Day'] > 1)

    # Calculate the customer retention rate
    return round(num_repeat_customers/num_customers *100,2)
