import pandas as pd

data = {
    "name": ["sana", "ali", "sara", "ahmed", "hina"],
    "marks": [85, 70, 90, 0, None]
}

ss = pd.DataFrame(data)

print("Complete table:")
print(ss)

print("\nMarks column:")
print(ss["marks"])

print("\nFirst 2 rows:")
print(ss.head(2))

print("\nTotal marks:")
print(ss["marks"].sum())

print("\nAverage marks:")
print(ss["marks"].mean())

print("\nMarks 85 or above:")
print(ss[ss["marks"] >= 85])

print("\nMarks between 70 and 85 — AND:")
print(ss[(ss["marks"] >= 70) & (ss["marks"] <= 85)])

print("\nAli or Ahmed — OR:")
print(ss[(ss["name"] == "ali") | (ss["name"] == "ahmed")])

print("\nAli or Sara — isin:")
print(ss[ss["name"].isin(["ali", "sara"])])

print("\nNames containing 'sa':")
print(ss[ss["name"].str.contains("sa", case=False, na=False)])

print("\nMissing marks:")
print(ss[ss["marks"].isna()])

print("\nAvailable marks — includes zero:")
print(ss[ss["marks"].notna()])
ss.to_csv("students.csv", index=False)
