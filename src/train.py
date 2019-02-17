import pandas as pd
from DataStat import Handeler


# ------------ Load Data --------------------------------------
df = Handeler()
path = "C:/Users/ali_a/Desktop/HIV-2019/GLO-7030_Deep_Learning/data/train.csv"
out = df.inputs(path)
#Delet all columns with zero and the ID
out = df._drop()
print("the number of raws that we have is : ",len(out))

#Seting our goal prediction
out.rename(columns = {'SalePrice':'default'}, inplace=True)
#Pandas make a column of index, we need to drop it
out=out.drop([out.columns[0]],axis=1)

df= out
#------------ Pre-Processing --------------------------------


#Create a new Class for Non Default observations.
df.loc[df.default == 0, 'nonDefault'] = 1
df.loc[df.default == 1, 'nonDefault'] = 0


#Create dataframes of only default and nonDefault observations.
Default = df[df.default == 1]
print("class created",Default[0:2])

NonDefault = df[df.nonDefault == 1]
print("class created")

# Set X_train equal to 80% of the observations that defaulted.
X_train = Default.sample(frac = 0.8)
count_Defaults = len(X_train)

# Add 80% of the not-defaulted observations to X_train.
X_train = pd.concat([X_train, NonDefault.sample(frac = 0.8)], axis = 0)

