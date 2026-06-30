"""
Sports Performance Analyzer

A data analysis script using NumPy and Pandas to evaluate player metrics.

Pipeline Overview:
1. Load & Inspect: Read 'players_stats.csv' and print structural metrics.
2. NumPy Calculations: Compute total, mean, and std of goals, individual goals
   per 90 minutes, and categorize scoring tiers via np.where().
3. Feature Engineering: Map results back to the DataFrame and add a
   'goal_contribution' column.
4. Pandas Analysis: Group by team totals, locate the top performer, and count categories.
5. Matrix Operations: Generate a 2D team-level array and find the top team with np.argmax().
6. Export: Sort by performance descending and save to 'players_final.csv'.
"""

import pandas as pd
import numpy as np

print(f'{"*"*53} 1. Load & Inspect {"*"*53}\n')

# • Load the dataset in a DataFrame (df)
df = pd.read_csv('players_stats.csv')
print(f'Shape:\n{df.shape}\n') # • Shape of DataFrame
print('Information:'); df.info() # • Information about the DataFrame
print(f'\nDescription:\n{df.describe()}') # · Description of the dataset.

print(f'\n{"*"*53} 2. Raw Calculations {"*"*53}\n')

# • Convert the goals column to numpy array
goals_as_arr = df['goals'].to_numpy()

# • Find sum, mean, std, goals per 90 min
sum_of_goals = np.sum(goals_as_arr)  # — Sum of all goals
mean_of_goals = np.mean(goals_as_arr) # — Mean of all goals
stdv_of_goals = np.std(goals_as_arr) # — Standard Deviation of all goals.

print(f"""Sum of Goals: {sum_of_goals}
Mean of Goals: {mean_of_goals}
Standard Deviation of Goals: {stdv_of_goals}\n""") # Print all the basic goal statistics

# Convert minutes to numpy array to prevent data alignment/mixing bugs
minutes_played_arr = df['minutes_played'].to_numpy()
print("name: avg_goal_per_90m")
goal_per_90 = (goals_as_arr/minutes_played_arr) * 90 # — Calculate normalized Goals per 90 minutes
for name,gpn in zip(df['player'], goal_per_90):
    print(f"{name}: {gpn:.2f}")

# • Use np.where() to flag players: "High Scorer" if goals > league mean, else "Average/Low"
flagging = np.where(goals_as_arr > mean_of_goals, "High Scorer", "Average/Low")
print()
for name,flag, goals in zip(df['player'], flagging, goals_as_arr):
    print(f"{name}: {flag} -> {goals} goals")

print(f'\n{"*"*53} 3. Feature Engineering {"*"*53}\n')

# • Add two new columns
df['goals_per_90'] = goal_per_90
df["scorer_category"] = flagging

# • Add 'goal_contribution'
df['goal_contribution'] = df['goals'] + df['assists']
print(df)

print(f'\n{"*"*53} 4. Analysis {"*"*53}\n')

# • find total goals and total assists per team
contribution_per_team = df.groupby(['team'])[['goals', 'assists']].sum()
print(f'Contributions of each team (goals+assists):')
print(contribution_per_team)

# • Find the player with the highest goals_per_90 (entire row)
indx = df['goals_per_90'].idxmax()
print(f'\nHighest scorer:\n{df.loc[indx]}')

# • Use value_counts() on scorer_category
count = df['scorer_category'].value_counts()
print(f'\nNumber of values in "scorer_category"\n{count}')

print(f'\n{"*"*53} 5. Team-Level Matrix {"*"*53}\n')

# • Extract team totals and convert to a 2D NumPy array
team_summary = df.groupby(['team'])[['goals', 'assists', 'matches_played']].sum()
team_summary_arr = team_summary.to_numpy()
print(f'Teams as a 2D numpy array:\n{team_summary_arr}\n')
# • Use np.argmax() on this array to find which team scored the most goals overall
highest_goals = np.argmax(team_summary_arr[:, 0])
top_team = team_summary.iloc[highest_goals]
print(f"Highest Goal scorer team is: {top_team.name}")
print(f"- Goals: {top_team['goals']}")
print(f"- Assists: {top_team['assists']}")
print(f"- Matches Played: {top_team['matches_played']}")

print(f'\n{"*"*53} 6. Save & Export {"*"*53}\n')

# • Sort by goals_per_90 in decending order
sorted_by_normalized_goals = df.sort_values("goals_per_90", ascending=False)

# • Export to players_final.csv
sorted_by_normalized_goals.to_csv('players_final.csv', index=False)
print(sorted_by_normalized_goals)
print(f"\nFinal Data has been stored as 'players_final.csv' in the directory.")
