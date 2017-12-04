import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, cross_validation, linear_model

df_canada = pd.read_csv('lookup.csv', header = 1)
df_canada1 = df_canada.iloc[:, :2]

df_us = pd.read_csv('DFF.csv')
df_us.columns = ['Date', 'US_I']
df_USD_CAD = pd.read_csv('USD CAD Historical Data.csv')

df_interest = pd.merge(df_canada1, df_us, how = 'inner', on = ['Date'])
df_interest['Date'] = pd.to_datetime(df_interest['Date'], format = '%Y-%m-%d')
df_interest.columns = ['Date', 'CAD_I', 'US_I']
df_USD_CAD['Date'] = pd.to_datetime(df_USD_CAD['Date'], format = '%b %d, %Y')

df_final = pd.merge(df_interest, df_USD_CAD, how = 'inner', on = ['Date'])

df_final['Future_EX'] = df_final['Price'].shift(7)
df_final = df_final[df_final.CAD_I != ' Bank holiday']
df_final.CAD_I = df_final.CAD_I.apply(float)
df_final['Interest_Diff'] = df_final['CAD_I'].subtract(df_final['US_I'])
df_final = df_final[['CAD_I', 'US_I', 'Price', 'Open', 'High', 'Low', 'Change %', 'Future_EX', 'Interest_Diff']].astype(float)
df_final.dropna(inplace = True)
X = np.array(df_final.drop(['Future_EX'],1))
X = preprocessing.scale(X)

y = np.array(df_final['Future_EX'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size =0.2)


clf = linear_model.LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print accuracy
