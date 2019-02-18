import os
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import LabelBinarizer

import datetime
from DataStat import Handeler
from pathlib import Path


sns.set()
# data import

df = Handeler()
out = df.inputs('../data/train.csv')

#Infor on type of variable
out.info()


#About out SalePrice distribution
g = sns.distplot(out['SalePrice'],norm_hist=True,fit=norm, kde=False)
plt.title('La distribution des prix - SalePrice',  fontsize = 24)
plt.xlabel('Prix ($)',fontsize=18)
plt.yticks(g.get_yticks(), (g.get_yticks() * 10000000).round(decimals=0))
plt.ylabel('Distribution [%]', fontsize=16)
plt.show()




#General information on the sale satisfaction

''' 
SaleCondition: Condition of sale

       Normal  Normal Sale
       Abnorml Abnormal Sale -  trade, foreclosure, short sale
       AdjLand Adjoining Land Purchase
       Alloca  Allocation - two linked properties with separate deeds, typically condo with a garage unit 
       Family  Sale between family members
       Partial Home was not completed when last assessed (associated with New Homes)
'''


out["SaleCondition"] = out["SaleCondition"].astype('category')
sns.catplot(x="SaleCondition", y="SalePrice", kind="box", data=out)

plt.title("le type de vente en fonction du prix")
plt.show()



# Influence of months sales on the total sales

sns.kdeplot(out['MoSold']);
plt.title("Influence mensuel sur les ventes de maisons")
plt.xlim(1,12)
plt.show()


'''
out["HouseStyle"] =out["HouseStyle"].astype('category')
out["HouseStyle"] =out["HouseStyle"].cat.codes

lb_style = LabelBinarizer()
lb_results = lb_style.fit_transform(obj_df["Hou"])
pd.DataFrame(lb_results, columns=lb_style.classes_).head()
'''
for name in (out.columns):
    if out[name].dtypes == "object":
        out[name]= out[name].astype('category')


# Count plots of categorical features
cat = out.select_dtypes(include=['category']).columns
f = pd.melt(out, id_vars=['SalePrice'], value_vars=sorted(cat[1:10]))

g = sns.FacetGrid(f, col='variable', col_wrap=3, sharex=False, sharey=True, size=3)
g = g.map(sns.boxplot, 'value', 'SalePrice')
[plt.setp(ax.get_xticklabels(), rotation=90) for ax in g.axes.flat]
g.fig.tight_layout()
plt.show()


out.info()

#Le nombre détage affect t-il le prix ?
# sns.factorplot(x = "1stFlrSF", y = "SalePrice", hue = "HouseStyle", kind = 'violin', col = "HouseStyle", data = out)
# plt.title("La superficie de la maison en fonction du prix")
# plt.show()

