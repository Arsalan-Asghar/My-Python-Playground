##  Pandas Mini-Project

**Project: Student Performance Analyzer**

Build a script that takes `students.csv` and produces a full analysis. This should feel like a real small data analysis task, not just isolated exercises.

---

### Requirements

**1. Load & Inspect**
- Load `students.csv`
- Print shape, info, and describe

**2. Clean (simulate real-world messiness)**
- Add 2-3 rows with missing `marks` values (you can append manually or create a second CSV and concat it)
- Handle the missing values appropriately (your choice: drop or fill — justify which one you picked in a comment)

**3. Feature Engineering**
- Add a `result` column (`Pass`/`Fail`) based on marks ≥ 60
- Add a `grade_letter` column recalculated using `apply()` + lambda based on marks (A ≥ 80, B ≥ 70, C otherwise) — even if `grade` already exists, recalculate it independently to verify consistency
- Add a `marks_normalized` column scaling marks to a 0–1 range: `(marks - min) / (max - min)`

**4. Analysis**
- Show average marks per grade using `groupby()`
- Show how many students passed vs failed
- Identify the top scorer (entire row, not just the name)
- Identify the lowest scorer (entire row)

**5. Sort & Export**
- Sort the final DataFrame by `marks` descending
- Save the final cleaned + processed DataFrame to a new CSV called `students_final.csv` using `to_csv()` (look up the syntax — it's `df.to_csv("filename.csv", index=False)`)
