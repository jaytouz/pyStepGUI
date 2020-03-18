from appJar import gui
from dfsteps.DfSteps import DfSteps
from iosteps.StepOutputStream import StepOutputStream
import os
import pandas as pd


class MainFrame:
    app = None
    data = None
    directory = "No file yet"
    def __init__(self, w, h):
        self.app = gui("Step file finder", (w,h))
        self.data = self.openFeather()
        self.app.addButton("printHead", self.head)
        self.app.addButton("ouvrir fichier de pas", self.findFolder)
        self.app.addButton("btnUp", self.update)

        self.app.label("directory", self.directory)

    def go(self):
        self.app.go()

    def head(self):
        self.data.head()

    def openFeather(self):
        path = self.app.openBox("Choisir les données sources", os.path.curdir, [("FEATHER File", "*.feather")])
        return DfSteps(pd.read_feather(path))

    def findFolder(self):
        self.directory = self.app.openBox("choisir un fichier de pas", os.path.curdir, [("Microsoft Excel Worksheet", "*.xlsx")])
        self.printFileName()

    def printFileName(self):
        self.app.label("Directory", self.directory)
        self.directory = "No file yet"

    def update(self):
        outputStream = StepOutputStream()
