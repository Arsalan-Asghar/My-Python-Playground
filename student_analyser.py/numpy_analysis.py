import numpy as np
from datetime import datetime

# 1. Setup Data
marks = np.random.randint(50, 100, size=(10, 5))

subject = np.array(["Machine Learning", "Probability and Statistics", 
                    "Database Management System", "Operating System", "Compiler Construction"])

student = np.array(["Arsalan Asghar", "Syed Minhaj", "Muhammad Farhan", 
                    "Muhammad Ahmed", "Hammad Memon", "Devraj Aswani", "Ameer Hamza", "Hitin Puri",
                    "Anas Dal", "Julius"])

# Generate a clean timestamp string
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report_lines = []
report_lines.append(f"Report Generated On: {timestamp}")
report_lines.append("=" * 50)
report_lines.append("------------Analysis-----------")
report_lines.append("=" * 50 + "\n")

# 2. Student-wise Analysis (Row by Row)
for name, mark in zip(student, marks):
    report_lines.append(f"Name: {name}")

    avg_per_student = np.mean(mark)
    highest_per_student = np.max(mark)
    lowest_per_student = np.min(mark)
    pass_or_fail = np.where(avg_per_student >= 60, "Pass", "Fail")

    for num, sub in zip(mark, subject):
        report_lines.append(f"  {sub}: {num}")

    report_lines.append(f"Mean of marks: {avg_per_student:.2f}")
    report_lines.append(f"Highest marks: {highest_per_student}")
    report_lines.append(f"Lowest marks: {lowest_per_student}")
    report_lines.append(f"{name}: {pass_or_fail}")
    report_lines.append("-" * 30 + "\n")

report_lines.append("=" * 50)
report_lines.append("------------Subject-wise Analysis-----------")
report_lines.append("=" * 50 + "\n")

# 3. Subject-wise Analysis (Column by Column via axis=0)
avg_per_sub = np.mean(marks, axis=0)
highest_per_sub = np.max(marks, axis=0)
lowest_per_sub = np.min(marks, axis=0)

for sub, avg, high, low in zip(subject, avg_per_sub, highest_per_sub, lowest_per_sub):
    report_lines.append(f"Average Score of {sub}: {avg:.2f}")
    report_lines.append(f"Highest Score of {sub}: {high}")
    report_lines.append(f"Lowest Score of {sub}: {low}")
    report_lines.append("-" * 30 + "\n")

report_lines.append("=" * 50)
report_lines.append("------------Overall Class Summary-----------")
report_lines.append("=" * 50 + "\n")

# 4. Global Records via Average Logic (Corrected!)
means = np.mean(marks, axis=1)

# Now it correctly tracks the top/bottom student based on overall average
report_lines.append(f"Top Scorer (Highest Average): {student[np.argmax(means)]} (Avg: {np.max(means):.2f})")
report_lines.append(f"Lowest Scorer (Lowest Average): {student[np.argmin(means)]} (Avg: {np.min(means):.2f})")
report_lines.append(f"Total average of the entire class is: {np.mean(marks):.2f}\n")

# 5. Write everything to report.txt
with open("report.txt", "w") as file:
    file.write("\n".join(report_lines))

print("Analysis successfully saved to report.txt.")

# 6. Finally, printing the output in terminal as well.
print('\n'.join(report_lines))