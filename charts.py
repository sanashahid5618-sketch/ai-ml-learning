import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("students.csv")
chart_data = students.dropna(subset=["marks"])
plt.bar(chart_data["name"], chart_data["marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()
