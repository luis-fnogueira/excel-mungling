import glob
from abc import ABC, abstractmethod


class MapValues(ABC):

    @abstractmethod
    def mapFilesInFolderByExtension(self, path: str, extension: str) -> list:
        """
        This functions maps the files in a path by its extentions. It inputs them
        into a list and returns the list. 
        """
        file_list = glob.glob(f'{path}' + f'/*{extension}')
        return file_list
