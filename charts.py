import matplotlib.pyplot as plt

names = ["Sana", "Ali", "Sara"]
marks = [85, 70, 90]

plt.bar(names, marks)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()