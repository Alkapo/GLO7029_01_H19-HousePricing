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
    def _drop(self):

        l_drop = self.data.columns[self.data.isnull().any()].tolist()
        for x in l_drop:
            self.data = self.data.drop([x],axis=1)
        self.data = self.data.drop(["Id"],axis=1)

        return self.data
    def correlation_matrix(df):
        from matplotlib import pyplot as plt
        from matplotlib import cm as cm

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        cmap = cm.get_cmap('jet', 30)
        cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
        ax1.grid(True)
        plt.title('Abalone Feature Correlation')
        labels=['Sex','Length','Diam','Height','Whole','Shucked','Viscera','Shell','Rings',]
        ax1.set_xticklabels(labels,fontsize=6)
        ax1.set_yticklabels(labels,fontsize=6)
        # Add colorbar, make sure to specify tick locations to match desired ticklabels
        fig.colorbar(cax, ticks=[.75,.8,.85,.90,.95,1])
        plt.show()

#This section is for test and by default it load data
if __name__ == '__main__':
    file = Handeler()
    path = "C:/Users/ali_a/Desktop/HIV-2019/GLO-7030_Deep_Learning/data/train.csv"
    out = file.inputs(path)
    #Test du commit pycharm
    #out = file._variabls()
    print("the number of variables that we have is : ",out)
    print(file._null()!=0)

    out = file._drop()
    print("the number of variables that we have is : ",out)
    Handeler.correlation_matrix(out)



