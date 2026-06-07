import numpy as np

arr: np.ndarray = np.random.randint(50, 101, size=(5, 4))
sub: np.ndarray = np.array(["Machine Learning", "Probability and Statistics", "Operating System", "Artificial Intelligence"])
students: list = ["Arsalan", "Minhaj", "Farhan", "Ahmed", "Devraj"]

print("Student Marks:\n")

for student, student_marks in zip(students, arr):
    print(f"{student}:")
    
    for subject, mark in zip(sub, student_marks):
        print(f"{subject}: {mark}")
    print()

print()
subject_averages = np.mean(arr, axis=0)

print("\nAverage score for each subject:")
for subject, avg in zip(sub, subject_averages):
    print(f"{subject}: {avg:.2f}")

print()
student_averages = np.mean(arr, axis=1)

print("Average score for each student:")
for student, avg in zip(students, student_averages):
    print(f"{student}: {avg:.2f}")

print()

print(f"Highest value from the dataset: {np.max(arr)}")
print(f"Lowest value from the dataset: {np.min(arr)}")
print()

print(f"Overall average of the dataset: {np.mean(arr)}")
print()

reshaped_dataset = arr.reshape(4,5)
print(f"Reshaped Array (5x4 -> 4x5):\n{reshaped_dataset}")
