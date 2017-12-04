import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm, preprocessing, cross_validation, linear_model
import math
import time 
import datetime

api_key = 'bU_9enYtXZ2FZVFxxfVC'

def create_labels(cur_hpi, fut_hpi):
	if fut_hpi > cur_hpi:
		return 1
	else:
		return 0
		
def moving_average(values):
	return values.mean()		

housing_data = pd.read_pickle('HPI.pickle')


housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace = True)
housing_data.dropna(inplace = True)

housing_data['US_HPI_future'] = housing_data['Value'].shift(-1)
housing_data.dropna(inplace=True)

housing_data['label'] = list(map(create_labels, housing_data['Value'], housing_data['US_HPI_future']))


housing_data['ma_apply_example'] = housing_data['M30'].rolling(center = False, window =10).apply(moving_average)
housing_data.dropna(inplace=True)

X = np.array(housing_data.drop(['label', 'US_HPI_future'], 1))
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size =0.2)


clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)




print(housing_data)
# plt.legend(loc =4)
# plt.show()



df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['Pct_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'Pct_change', 'Adj. Volume']]



forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)


forecast_out = int(math.ceil(0.01*len(df)))
print forecast_out

df['label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace = True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

clf = linear_model.LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
with open('linearregression.pickle', 'wb') as f:
	pickle.dump(clf, f)



accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)


print (forecast_set, accuracy, forecast_out)

df['Forecast'] =np.nan

last_date =df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
	next_date = datetime.datetime.fromtimestamp(next_unix)
	next_unix+= one_day
	df.loc[next_date] = [np.nan for _ in range(len(df.columns) -1)] +[i]
	
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
