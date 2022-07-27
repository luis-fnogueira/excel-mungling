import pandas as pd


class DropColumns:

    def dropColumnsNotInList(self, dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:

        for column in dataframe:
            if column not in columns:
                dataframe.drop(column, axis=1, inplace=True)

        return dataframe


    def dropColumnsInList(self, dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:

        for column in dataframe:
            if column in columns:
                dataframe.drop(column, axis=1, inplace=True)

        return dataframe
