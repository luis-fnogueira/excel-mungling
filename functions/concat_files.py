from map_values import MapValues
import pandas as pd


class ConcatFiles(MapValues):


    # Overriding abstract method.
    def mapFilesInFolderByExtension(self, path: str, extension: str) -> list:
        return super().mapFilesInFolderByExtension(path, extension)


    def concatXlsxInPandasDataframe(self, files: list) -> pd.DataFrame:
        """This functions concatenates xlsx files in a Pandas Dataframe. It ONLY
           accepts .xlsx files. Engine=openpyxl is necessary because Pandas has
           deprecated reading .xlsx files in read_excel.
           Source: https://bit.ly/3otVV94"""
        
        xlsx_list = []
    
        for file in files:
            xlsx_list.append(pd.read_excel(file, engine="openpyxl"))

        return pd.concat(xlsx_list, ignore_index=True)
