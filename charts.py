import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("students.csv")

chart_data = students.dropna(subset=["marks"])

top_students = chart_data[chart_data["marks"] >= 80]

plt.bar(top_students["name"], top_students["marks"])

plt.title("Top Students")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("top_students.png")
plt.show()
