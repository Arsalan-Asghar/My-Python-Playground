## Project: Sports Performance Analyzer (NumPy + Pandas)

### Dataset setup

Create a CSV `players_stats.csv` with realistic-but-made-up data, something like:

```
player,team,matches_played,goals,assists,minutes_played
Player1,Team A,10,6,3,850
Player2,Team A,9,2,5,720
...
```

Make up **10 players**, across **3-4 teams**, with varying stats. You decide the exact numbers.

---

### Requirements

**1. Load & Inspect (Pandas)**
- Load the CSV, print `shape`, `info()`, `describe()`

**2. NumPy — Raw Calculations**
- Convert the `goals` column to a NumPy array using `.to_numpy()` or `.values`
- Use NumPy to calculate: total goals (league-wide), mean goals, the **standard deviation** of goals (new function — look up `np.std()`), and goals per 90 minutes for each player (`goals / minutes_played * 90`) using vectorized operations
- Use `np.where()` to flag players as `"High Scorer"` if goals > league mean, else `"Average/Low"` — store this as a NumPy array

**3. Pandas — Feature Engineering**
- Add the NumPy results back into the DataFrame as new columns: `goals_per_90`, `scorer_category`
- Add a `goal_contribution` column = `goals + assists`

**4. Pandas — Analysis**
- `groupby("team")` to find total goals and total assists per team
- Find the player with the highest `goals_per_90` (entire row)
- Use `value_counts()` on `scorer_category`

**5. NumPy — Team-Level Matrix (optional challenge)**
- Build a NumPy 2D array manually where each row is `[team_total_goals, team_total_assists, team_total_matches]` for each team (you'll need to extract these via Pandas groupby first, then convert to a NumPy array)
- Use `np.argmax()` on this array to find which team scored the most goals overall

**6. Sort & Export**
- Sort by `goals_per_90` descending
- Export to `players_final.csv`
