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

print("\n\n")


#datasets

df = pd.read_csv("datasets/student.csv")
print(df.head())
print("\n\n")
print(df.describe())
print("\n\n")
print(df.info())
print("\n\n")
print(df["Age"])
print("\n\n")
print("\n\n")
print("\n\n")
