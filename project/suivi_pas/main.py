
import os
import pandas as pd

from GUI.MainFrame import MainFrame
from dfsteps.DfSteps import DfSteps
from iosteps.StepOutputStream import StepOutputStream


def main():

    app = MainFrame(200,200)
    app.go()


    # curdir = os.path.curdir
    # fileName = "suivi_pas.xlsx"
    # feather_fileName = "./feather"
    # path = ''.join([curdir, "/", fileName])
    # df = pd.read_excel(path, usecols = [0,1,2,3,4,5])
    #
    #
    #
    # print(df.head())
    # df_f = pd.read_feather(feather_fileName)
    # print(df_f.tail())
    # streamOut = StepOutputStream(df, feather_fileName)
    # streamOut.update_output()
    #
    #
    # #
    # #
    # # df1 = df.copy()    # df_f = pd.read_feather(feather_fileName)
    # #     # print(df_f.iloc[229])
    # # print(df.size)
    # #
    # # print(df.iloc[229])

if __name__ == "__main__":
    main()