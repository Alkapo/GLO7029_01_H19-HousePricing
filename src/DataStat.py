import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

class Handeler():
    def __init__(self):
        super(Handeler, self).__init__()
        self.data = None

    #Set the dataframe
    def inputs(self,path):
        self.data = pd.read_csv(path)
        #List of varibales in my dataset
        return self.data

    #get columns name
    def _variabls(self):
        return self.data.columns.values.tolist()
    def _null(self):
        return self.data.isnull().sum()


if __name__ == '__main__':
    file = Handeler()
    path = "C:/Users/ali_a/Desktop/HIV-2019/GLO-7030_Deep_Learning/data/train.csv"
    out = file.inputs(path)
    out = file._variabls()
    print("the number of variables that we have is : ",len(out))
    print(np.where())
