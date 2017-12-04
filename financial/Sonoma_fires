####Projected price and rent changes after sonoma fires

###Data on housing prices and rent in Sonoma County past March 2017 are not released yet- 
###Projections will look for comparison to realtiy

import quandl
import pandas as pd
import numpy as np

housing_inventory_sonoma=quandl.get('ZILLOW/CO99_IMP')
housing_price_sonoma= quandl.get('ZILLOW/CO99_MLPAH')
housing_rent_sonoma= quandl.get('ZILLOW/CO99_MRPAH')

inventory=pd.DataFrame(housing_inventory_sonoma)
price=pd.DataFrame(housing_price_sonoma)
rent =pd.DataFrame(housing_rent_sonoma)

price_vs_inventory = pd.concat([inventory, price], axis=1, join_axes = [price.index]).dropna()
price_vs_inventory.to_csv('sonoma_price_vs_inv.csv')
X = (price_vs_inventory.iloc[:,0]).reshape(-1, 1)
y = (price_vs_inventory.iloc[:,1]).reshape(-1, 1)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)
clf = linear_model.LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
print clf.coef_

rent_vs_inv = pd.concat([inventory, rent], axis=1, join_axes = [rent.index]).dropna()
rent_vs_inv.to_csv('sonoma_rent_vs_inv.csv')
X = (rent_vs_inv.iloc[:,0]).reshape(-1, 1)
y = (rent_vs_inv.iloc[:,1]).reshape(-1, 1)


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.1)
clf = linear_model.LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
print clf.coef_


###Using Linear Regression, we find that for every increase of unit inventory, there is a drop in approximately $100 in Price
### and $.34 in monthly rent
### Assuming a 5% drop in inventory from a March basis of 500(drop of 25), we expect Prices to increase $2500 and rent to increase by $7.28

###We throw our results into R using summary(lm(Price~Inv)) and summary(lm(Rent~Inv)) and get:
###Price: (R^2: .1021, Inv_Pr = .05) Thus changes in inventory only account for approx. 10% of price change with 95% confidence
###Rent:  (R^2: .3277, Inv_Pr = 000) Thus changes in invetory account for approx. 33% of rent change with 100% confidence
