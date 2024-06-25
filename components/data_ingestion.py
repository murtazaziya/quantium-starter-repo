import pandas as pd

df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

df1 = df1[df1['product'] == 'pink morsel']
df2 = df2[df2['product'] == 'pink morsel']
df3 = df3[df3['product'] == 'pink morsel']

df1['price'] = df1['price'].str.replace('$', '').astype(float)
df2['price'] = df2['price'].str.replace('$', '').astype(float)
df3['price'] = df3['price'].str.replace('$', '').astype(float)

df1['quantity'] = pd.to_numeric(df1['quantity'])
df2['quantity'] = pd.to_numeric(df2['quantity'])
df3['quantity'] = pd.to_numeric(df3['quantity'])

df1['sales'] = df1['price'] * df1['quantity']
df2['sales'] = df2['price'] * df2['quantity']
df3['sales'] = df3['price'] * df3['quantity']

df1.drop(['price', 'quantity', 'product'], axis=1, inplace=True)
df2.drop(['price', 'quantity', 'product'], axis=1, inplace=True)
df3.drop(['price', 'quantity', 'product'], axis=1, inplace=True)

df = pd.concat([df1, df2, df3], ignore_index=True)

df.to_csv('data/data.csv')