# Importing Pandas library
import pandas as pd

# Creating two lists
author = ['Jitender', 'Purnima',
		'Arpit', 'Jyoti']
article = [210, 211, 114, 178]

# Creating two Series by passing lists
auth_series = pd.Series(author)
article_series = pd.Series(article)

# Creating a dictionary by passing Series objects as values
frame = {'Author': auth_series,
		'Article': article_series}

# Creating DataFrame by passing Dictionary
result = pd.DataFrame(frame)

# Printing elements of Dataframe
print(result)
#Custom index values.

import pandas as pd
dict = {'names':['ratan','ramu','raju'],
'numbers':[1,2,3],
'fruits':['apple','mango',"orange"]}
df = pd.DataFrame(dict,index=['A','B','C'])
print(df)
#to csv file

import pandas as pd
dict = {'names':['ratan','ramu','raju'],
'numbers':[1,2,3],
'fruits':['apple','mango',"orange"]}
df = pd.DataFrame(dict,index=['A','B','C'])
df.to_csv('abc.csv')
print(df)
import pandas as pd
df1 = pd.DataFrame({
"Company Name":["Google", "Microsoft", "SpaceX","Amazon","Samsung"],
"Founders":['Larry Page','Bill Gates','Elon Musk','Jeff Bezos', 'Lee Byungchul'],
"Founded": [1998, 1975, 2002, 1994, 1938],
"Number of Employees": [103459, 144106, 6500647,50320,67145]})
df2 = pd.DataFrame({
'Company Name':['WhatsApp'],
'Founders':['Jan Koum, Brian Acton'],
'Founded': [2009],
'Number of Employees': [5000]}, index=['i'])
res = df1._append(df2,ignore_index = True)
print(res)
data = res

print(data)
print(data.columns)
print(data.dtypes)

print(data.shape) # printing rows & columns
print(data.shape[0]) # to print rows
print(data.shape[1]) # to print column

print(data.head())
print(data.head(2))

print(data.tail())
print(data.tail(1))

print(data[0:4])
print(data[3:])
print(data[:4])
print(data[data['Number of Employees'] > 10000][['Company Name', 'Founders', 'Founded', 'Number of Employees']])
print(data[data.Founded > 2000][['Company Name', 'Founders', 'Founded', 'Number of Employees']])
print(data.iloc[2,3])
print(data.iloc[1,2])

print(data.at[3,'Founders'])

print(data.iat[1,1])
print(data.iat[2,2])

import numpy as np
import matplotlib.pyplot as matplt
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C = np.array(cvalues)
matplt.plot(C)
matplt.show()
