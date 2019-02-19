import os
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from DataStat import Handeler

from pathlib import Path

def correlation(data):
    corr = data.corr()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, len(data.columns), 1)
    ax.set_xticks(ticks)
    plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data.columns)
    ax.set_yticklabels(data.columns)
    plt.show()

def matrixplot(data):
    # scatter plot matrix
    pd.plotting.scatter_matrix(data)
    plt.show()

if __name__ == '__main__':

    # Get current path
    mypath = Path().absolute()
    mypath = os.path.abspath(os.path.join(mypath, os.pardir))
    path = mypath + "/data/train.csv"

    df = Handeler()
    out = df.inputs(path)

    # principal attributs
    price = out[['SalePrice', 'YrSold']]
    # boxplot
    price.boxplot(by="YrSold", column="SalePrice")
    matrixplot(price)

    # principal attributs
    general = out[['Id', 'SalePrice', 'YearBuilt', 'LotArea', 'OverallCond', 'OverallQual', 'YrSold']]
    #correlation(general)
    #matrixplot(general)

    # Localisation
    zone = out[['Id', 'SalePrice', 'MSZoning', 'LotFrontage', 'Street', 'Alley', 'Neighborhood', 'Condition1', 'Condition2']]
    #correlation(zone)
    #print(zone)

    # Area
    area = out[['Id', 'SalePrice', 'LotArea', 'LandSlope']]
    #correlation(area)

    # Building
    building = out[['Id', 'SalePrice', 'MSSubClass', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond']]
    #correlation(building)

    # Roof
    roof = out[['Id', 'SalePrice', 'YearRemodAdd', 'RoofStyle', 'RoofMatl']]
    #correlation(roof)

    # Exterior
    exterior = out[['Id', 'SalePrice', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation']]
    #correlation(exterior)

    # basement
    basement = out[['Id', 'SalePrice', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF']]
    #correlation(basement)

    # heating and CentralAir
    airCondition = out[['Id', 'SalePrice', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'Functional', 'Fireplaces', 'FireplaceQu']]
    #correlation(airCondition)

    # building size
    #size = out[['Id', 'SalePrice', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'Bedroom', 'Kitchen', 'KitchenQual', 'TotRmsAbvGrd']]
    #correlation(size)

    # garage
    garage = out[['Id', 'SalePrice', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive']]
    #correlation(garage)

    # porch
    porch = out[['Id', 'SalePrice', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch']]
    #correlation(porch)

    # pool and others equipement
    pool = out[['Id', 'SalePrice', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal']]
    #correlation(pool)

    # sale
    sale = out[['Id', 'SalePrice', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition']]
    correlation(sale)

    # others
    others = out[[]]


