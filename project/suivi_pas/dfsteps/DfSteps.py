import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DfSteps:
    weekday = {0:"lundi",
               1:"mardi",
               2:"mercredi",
               3:"jeudi",
               4:"vendredi",
               5:"samedi",
               6:"dimanche"}

    month = {1:"janvier", 2:"fevrier", 3:"mars",
             4:"avril", 5:"mai", 6:"juin", 7:"juillet",
             8:"aout", 9:"septembre", 10:"octobre", 11:"novembre",
             12:"decembre"}

    year = {2019}

    df = None
    def __init__(self, df):
        self.df = df

    def head(self, window=5):
        print(self.df.head(window))

    def removeNaN(self):
        self.df.steps.fillna(self.getMeanSteps(), inplace=True)

    def plotDistSteps(self):
        sns.distplot()

    def getMeanSteps(self):
        return self.steps.mean()

    def steps(self):
        return self.df.steps

    def stars(self):
        return self.df.stars

    def plotGroupBy(self, by, header, borne_inf, borne_sup):
        mean = self.df[header].mean()
        median = self.df[header].median()
        try:
            idx = pd.IndexSlice
            ax = plt.subplot()
            self.df.groupby(by).mean().loc[idx[borne_inf:borne_sup], header].plot()
            plt.hlines(mean, xmin=borne_inf, xmax=borne_sup)
            plt.hlines(median, xmin=borne_inf, xmax=borne_sup, color='r')
            ax.set_ylabel(header)
            plt.show()
        except Exception as e:
            print("verifier les noms et l'etendu du groupement")
            print(e)

    def getCountStepsUnder(self, value):
        return self.df[self.df.steps <= value].count()[0]

    def getCountStepsOver(self, value):
        return self.df[self.df.steps >= 4000].count()[0]

    def getCountStepsBetween(self, lower, upper):
        return self.df[(self.df.steps >= lower) & (self.df.steps <= upper)].count()[0]


