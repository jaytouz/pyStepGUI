# class enfant de StepStream. Permet de lire les données du fichier excel
from iosteps.StepStream import StepStream
import pandas as pd
import traceback


class StepInputStreamFromExcel(StepStream):

    _df_input = None; # dataframe qui va être lu

    def __init__(self, xlsxFilePath):
        return

    @property
    def df_input(self, xlsxFilePath):
        return self._df_input

    @df_input.setter
    def df_input(self, xlsxFilePath):
        if xlsxFilePath is None:
            self._df_input = None
        else:
            try:
                self._df_input = pd.read_excel(xlsxFilePath)
            except Exception as e:
                traceback.print_exc()

    def __del__(self):
        self.df_input(None)
        print("input deleted...")









