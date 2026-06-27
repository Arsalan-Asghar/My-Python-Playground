import pandas as pd

"""
Student Performance Analyzer:
Loads student exam data, cleans missing values, engineers new features
(pass/fail result, recalculated grade, normalized marks), and analyzes
performance by grade. Outputs a sorted, cleaned dataset to a new CSV.
"""

# • Load the dataset
df = pd.read_csv("students.csv") 

print(f"{"*"*13} 1. Load & Inspect {"*"*13}\n")

print(f"Shape: {df.shape}\n")  # • Check orientation of the imported dataset
print("Info:")
df.info() # • Prints data types and missing value counts automatically

print(f"\nDescription:\n{df.describe()}\n") 

print(f"{"*"*13} 2. Clean (simulate real-world messiness) {"*"*13}\n")

# • Load manual/incomplete data to append
notComplete_data = pd.read_csv('incomplete_data.csv') 
print(f"Incomplete Data:\n{notComplete_data}\n") 

# • Merge datasets together
df_combined = pd.concat([df, notComplete_data], ignore_index=True) 
print(f"Newly made data:\n{df_combined}\n") 

# • Drop rows missing 'marks' to prevent math errors during aggregation (mean, sum, etc.)
df_cleaned = df_combined.dropna(subset=["marks"])  # subset=["marks"] helps Remove the row with NaN in 'marks' column
print(f"Cleaned/Fixed Data:\n{df_cleaned}\n")

print(f"{"*"*13} 3. Feature Engineering {"*"*13}\n")

# • Added new column called 'result' which shows pass if marks >= 60
df_cleaned["result"] = df_cleaned['marks'].apply(lambda x: "passed" if x>=60 else "failed")

# • Assigning grades independently for checking integrity later with already available grades in the dataset.
df_cleaned['grade_letter'] = df_cleaned["marks"].apply(lambda x: "A" if x>=80 else "B" if x>=70 else "C")
similarity_check = df_cleaned["grade"] == df_cleaned["grade_letter"] #  • Checking integrity of grades.
print('Similarity checking:')
print(f"{similarity_check}\n")

# • Add a 'marks_normalized' column scaling marks to a 0–1 range: (marks - min) / (max - min)
numerator = df_cleaned['marks'] - df_cleaned["marks"].min()
denominator = df_cleaned['marks'].max() - df_cleaned["marks"].min()
# Added the new column with its values we'll get from the formula
df_cleaned['marks_normalized'] = numerator/(denominator if denominator !=0 else 1)
print(f"Updated Data:\n{df_cleaned}\n")

print(f"{"*"*13} 4. Analysis {"*"*13}\n")

# • Show average marks per grade using groupby()
avg_marks_per_grade = df_cleaned.groupby('grade').agg({'marks': "mean"})
print(f"Average marks per grade:\n{avg_marks_per_grade}\n")

# • Show how many students passed vs failed
passed = (df_cleaned['result'] == 'passed').sum()
failed = (df_cleaned['result'] == 'failed').sum()
print(f"Number of passed students: {passed}")
print(f"Number of failed students: {failed}\n")

# • Identify the top scorer (entire row, not just the name)
# idxmax() is to find the index of maximun value of the specific column. In this case, it's 'marks.'
top_scorer = df_cleaned['marks'].idxmax() # loc is to find the exact row of what we add as it's parameter.
print(f"Top Scorer:\n{df_cleaned.loc[top_scorer]}\n") 

# · Identify the lowest scorer (entire row)
lowest_scorer = df_cleaned['marks'].idxmin()
print(f"Lowest Scorer:\n{df_cleaned.loc[lowest_scorer]}\n")

print(f"{"*"*13} 5. Sort & Export {"*"*13}\n")

# Sort the final DataFrame by marks descending
df_sorted = df_cleaned.sort_values('marks', ascending=False)
print(f"Final cleaned and sorted data:\n{df_sorted}\n")

# · Save the final cleaned + processed DataFrame to a new CSV called students_final.csv
df_sorted.to_csv("students_final.csv", index=False) 
print(f"Final Data has been stored as 'students_final.csv' in the directory.")
