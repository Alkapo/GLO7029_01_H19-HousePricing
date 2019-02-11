import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from DataStat import Handeler



df = Handeler()
path = "C:/Users/ali_a/Desktop/HIV-2019/GLO-7030_Deep_Learning/data/train.csv"
out = df.inputs(path)
#Delet all columns with zero and the ID
out = df._drop()
print("the number of raws that we have is : ",len(out))

#Seting our goal prediction
out.rename(columns = {'SalePrice':'default'}, inplace=True)
#Pandas make a column of index, we need to drop it
out =out.drop([out.columns[0]],axis=1)

