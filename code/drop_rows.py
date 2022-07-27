import pandas as pd


class DropRows():

    def dropRowsNotInList(self, dataframe: pd.DataFrame, column: str,
                          row_values: list) -> pd.DataFrame:

        return dataframe[~dataframe[column].isin(row_values)]

    
    def dropRowsInList(self, dataframe: pd.DataFrame, column: str,
                       row_values: list) -> pd.DataFrame:

        return dataframe[dataframe[column].isin(row_values)]
