#class pour ecrire vers donnees de pas vers un fichier txt
from iosteps.StepStream import StepStream
import os
import pandas as pd


class StepOutputStream(StepStream):
    path_to_file = None
    _fileName = None
    _df_output = None

    def __init__(self, df_output, path_to_file):
        self.path_to_file = path_to_file #path to file + fileName
        self.df_output= df_output

    @property
    def df_output(self):
        return self._df_output

    @df_output.setter
    def df_output(self, df):
        self._df_output = df

    def get_file_data(self)->pd.DataFrame:
        return pd.read_feather(self.path_to_file)

    def save_file_data(self):
        df = self.df_output
        df.to_feather(self.path_to_file +".feather")

    def update_output(self):
        df_ref = self.get_file_data()
        N = df_ref.shape[0]
        i = 0
        if self.df_output.shape[0] < df_ref.shape[0]:
            print("output file smaller, some data might have been overwritten")
            self.save_file_data()
        else:
            while (i < N-1 and any(self.df_output.loc[i] == df_ref.iloc[i])):
                i+=1
                print(i, df_ref.shape[0], self.df_output.shape[0])

            if (i==N):
                # rendu jusqua la fin sans diff, donc pas updater
                print("Pas de nouvelle donnée. Aucune modification")
            else:
                #sinon append du premier different jusqu'a la fin du nouveau df.output
                from_index = i
                new_df = pd.concat([df_ref, self.df_output.iloc[from_index:]], ignore_index=True)
                print(new_df)
                self.df_output = new_df
                print(self.df_output)

                self.save_file_data()
                print("Updated")






                



