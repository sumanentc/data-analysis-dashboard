import pandas as pd
from filter_by_year_and_quarter import filter_by_year_and_quarter

# Write a function to find the most profitable product for a given year and quarter
def most_profitable_product(data: pd.DataFrame, year: int, quarter: int) -> str:
    """
    Find the most profitable product for a given year and quarter
    :param data: The dataframe containing the data
    :param year: The year to find the most profitable product for
    :param quarter: The quarter to find the most profitable product for
    :return: The most profitable product for the given year and quarter
    """
    # Filter the data by the given year and quarter
    data = filter_by_year_and_quarter(data, year, quarter)

    # Find the most profitable product
    total_price_by_stock_code = pd.DataFrame(data.groupby('StockCode')['TotalPrice'].sum())
    #print(total_price_by_stock_code.head())
    sorted_by_price_stock = total_price_by_stock_code.sort_values(by='TotalPrice', ascending=False)
    #print(sorted_by_price_stock.head())
    return data.loc[data['StockCode'] == sorted_by_price_stock.index[0],'Description'].values[0]
