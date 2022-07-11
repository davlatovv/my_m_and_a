import sqlite3 
import pandas as pd 

def my(data1, data2, data3, connect):
  conn = sqlite3.connect(f'{connect}')
  df1 = pd.read_csv(f'{data1}')
  df2 = pd.read_csv(f'{data2}',sep=';', header=None, names=['Age', 'City', 'Gender', 'FirstName', 'Email', 'LastName', 'UserName', 'Country'])
  df3 = pd.read_csv(f'{data3}',sep='\t', skiprows=1, names=['Gender', 'FirstName', 'Email', 'Age', 'City', 'Country', 'LastName', 'UserName'])

  new = df2.FirstName.str.split(expand=True)
  df2.FirstName, df2.LastName, df2.UserName, df2.Age = new[0], new[1] ,new[0], df2.Age.str.replace('\D', '')
  new2 = df3.FirstName.str.split(expand=True)
  df3.Gender, df3.FirstName, df3.LastName, df3.UserName, df3.Email, df3.Age, df3.City = df3.Gender.str.replace('\w+_',''), new2[0].str.replace('\w+_',''), new2[1] ,new2[0].str.replace('\w+_',''), df3.Email.str.replace('\w+g_',''), df3.Age.str.replace('\w+_',''), df3.City.str.replace('\w+g_','')
  df3.Age = df3.Age.str.replace('\D', '')
  df = pd.concat([df1,df2,df3])

  gender = {'0': 'Female', '1': 'Male', 'F' : 'Female', 'M': 'Male'}
  df.Gender, df.FirstName, df.LastName, df.UserName, df.Email, df.City, df.Country = df.Gender.replace(gender), df.FirstName.str.replace('\W', ''), df.LastName.str.replace('\W', ''), df.UserName.str.replace('\W', ''), df.Email.str.lower(), df.City.str.replace('_', '-'), 'USA'
  df.FirstName, df.LastName, df.UserName, df.City = df.FirstName.str.title(), df.LastName.str.title(), df.UserName.str.lower(), df.City.str.title()
  
  return df.to_sql('customers', conn, index=False)

my('only_wood_customer_us_1.csv', 'only_wood_customer_us_2.csv', 'only_wood_customer_us_3.csv','plastic_free_boutique.sql')


