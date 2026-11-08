subjects = ["eng", "maths", "urdu"]

print("Original list:", subjects)

print("Total subjects:", len(subjects))

print("Second subject:", subjects[1])
print("Last subject:", subjects[-1])

subjects.append("python")
print("After append:", subjects)
print("Total subjects:", len(subjects))

subjects.insert(0, "computer")
print("After insert:", subjects)

subjects.remove("maths")
print("After remove:", subjects)

removed_subject = subjects.pop(1)
print("Removed subject:", removed_subject)
print("After pop:", subjects)

subjects.reverse()
print("After reverse:", subjects)

print("Final total subjects:", len(subjects))