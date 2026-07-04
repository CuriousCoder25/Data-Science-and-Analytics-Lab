import pandas as pd

series = pd.Series([1,2,3,4,5,6])
print("Pandas Series:")
print(series)

#dataframe creation
data = {
    "Name":["Gaurav","Pino","Evren"],
    "Age":[21,20,22],
    "City":["Dhangadhi","Mosk","Rimuru"]

}
print("\n\n")
df = pd.DataFrame(data)
print(df)