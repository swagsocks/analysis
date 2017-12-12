
### target RMSE .15

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


data=pd.read_csv('~/housing_prices/train.csv')
data.corr()['SalePrice']

sns.distplot(data['SalePrice'])
plt.show()
print("Skewness: %f" % data['SalePrice'].skew())
print("Kurtosis: %f" % data['SalePrice'].kurt())

#abs(feature) > .3 correlation
sns.set()
cols = ['SalePrice', 'LotFrontage', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',  'BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'Fireplaces', 'GarageYrBlt', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'FullBath']
corrmat = data[cols].corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()

#take out features with high collinearity
sns.set()
cols2 = ['SalePrice', 'LotFrontage', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',  'BsmtFinSF1', 'TotalBsmtSF', 'Fireplaces', 'OverallQual', 'GrLivArea', 'GarageCars', 'WoodDeckSF', 'OpenPorchSF', 'FullBath']
corrmat = data[cols2].corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()

#find all missing data- which features are we using?

total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)

#LotFrontage     259  0.177397
#MasVnrArea        8  0.005479 .5% of sample data - drop
#what other data points that we have are highly correlated to these features?

data.corr()['LotFrontage']
#1stFlrSF at .45 (TotalBsmtSF) is colinear
regr = linear_model.LinearRegression()
LotFrontage_X_train =  data[data['LotFrontage'].isnull() == False]['1stFlrSF']
LotFrontage_y_train = data[data['LotFrontage'].isnull() == False]['LotFrontage']
LotFrontage_X_pred = data[data['LotFrontage'].isnull() == True]['1stFlrSF']
regr.fit(LotFrontage_X_train.reshape(-1,1), LotFrontage_y_train)
indexes_Na = data[data['LotFrontage'].isnull() == True].index
Lot_predictions = pd.Series(regr.predict(LotFrontage_X_pred.reshape(-1,1)))
values = dict(zip(indexes_Na, Lot_predictions))

data['LotFrontage'].fillna(value = values, inplace = True)

MasVnr_Na = data[data['MasVnrArea'].isnull()==True]
data_cleaned = pd.concat([data, MasVnr_Na]).drop_duplicates(keep = False)

#See heatmap again

sns.set()
cols =  ['SalePrice', 'LotFrontage', 'YearBuilt', 'YearRemodAdd',  'BsmtFinSF1', 'TotalBsmtSF', 'Fireplaces', 'OverallQual', 'GrLivArea', 'GarageCars', 'WoodDeckSF']
corrmat = data_cleaned[cols].corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()

data_cleaned['SalePrice'] = np.log(data_cleaned['SalePrice'])

cols.remove('SalePrice')
for x in features:
	plt.scatter(data_cleaned[x], data_cleaned['SalePrice'])
	plt.xlabel(x, fontsize=18)
	plt.ylabel('SalePrice', fontsize=18)
	plt.show()


from sklearn.linear_model import LogisticRegression #logistic regression
from sklearn import svm #support vector Machine
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.naive_bayes import GaussianNB #Naive bayes
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix, mean_squared_error, r2_score #for confusion matrix

train,test=train_test_split(data_cleaned,test_size=0.3,random_state=0)
train_X=train[cols]
train_Y=train['SalePrice']
test_X=test[cols]
test_Y=test['SalePrice']
X=data_cleaned[cols]
Y=data_cleaned['SalePrice']

regr.fit(train_X, train_Y)
y_pred = regr.predict(test_X)
print('Variance score: %.2f' % r2_score(test_Y, y_pred))










validation_data=pd.read_csv('~/housing_prices/test.csv')

LotFrontage_X_train_val =  validation_data[validation_data['LotFrontage'].isnull() == False]['1stFlrSF']
LotFrontage_y_train_val = validation_data[validation_data['LotFrontage'].isnull() == False]['LotFrontage']
LotFrontage_X_pred_val = validation_data[validation_data['LotFrontage'].isnull() == True]['1stFlrSF']
regr.fit(LotFrontage_X_train_val.reshape(-1,1), LotFrontage_y_train_val)
indexes_Na_val = validation_data[validation_data['LotFrontage'].isnull() == True].index
Lot_predictions_val = pd.Series(regr.predict(LotFrontage_X_pred_val.reshape(-1,1)))
values_val = dict(zip(indexes_Na_val, Lot_predictions_val))



validation_data['LotFrontage'].fillna(value = values_val, inplace = True)


validation_data['BsmtFinSF1'].fillna(value = 0, inplace = True)
validation_data['TotalBsmtSF'].fillna(value = 0, inplace = True)
validation_data['GarageCars'].fillna(value = 0, inplace = True)


validation_data['MasVnrArea'].fillna(value = 0, inplace = True)


validation_data_cleaned = validation_data

X_test_val = validation_data_cleaned[cols]


regr.fit(X, Y)
y_pred_val = regr.predict(X_test_val)
results = pd.DataFrame(np.exp(y_pred_val), index = validation_data['Id'])
results.columns = ['SalePrice']
results.to_csv('submission_housing_prices.csv')
