import pandas as pd 

file = "C:\Users\Lenovo\Downloads\pib por municipio.xlsx"

df = pd.read_excel(file, nrows=100)

print(df.head())