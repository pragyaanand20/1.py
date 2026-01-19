import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())

df["Grade"] = ["A", "A+", "A"]
print(df.sort_values("Marks"))

df.to_csv("students.csv", index=False)