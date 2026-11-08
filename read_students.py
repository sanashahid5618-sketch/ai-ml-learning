import pandas as pd

students = pd.read_csv("students.csv")

print(students)
print(students.isna().sum())

clean_students = students.dropna(subset=["marks"])
print(clean_students)
print(students.dtypes)
students["marks"] = pd.to_numeric(students["marks"])
students["marks"] = pd.to_numeric(students["marks"], errors="coerce")
print(students)