import os, os.path
import random
import sys
from datetime import datetime, date 
import math

if len(sys.argv) < 3:
    print("Usage: python info.py <name> <age>")
    sys.exit()

os.makedirs(os.path.join('ml_projects', 'data'), exist_ok=True)
os.makedirs(os.path.join('ml_projects', 'logs'), exist_ok=True)

name = sys.argv[1]
date_now = datetime.now().strftime("%d-%m-%Y" " %H:%M:%S")
data_points = sys.argv[2]
r_float = [random.uniform(1.0, 100.00) for _ in range(int(data_points))]
str_floats = '\n'.join(f"{num:.2f}" for num in r_float)
sum_of_r_float = math.fsum(r_float)
avg_of_r_float = sum_of_r_float/ len(r_float)
sqrt_of_r_float = math.sqrt(avg_of_r_float)

file_name_data = f'data_{date.today()}.txt'
file_path_data = os.path.join('ml_projects', 'data', file_name_data)

with open(file_path_data, 'w') as file:
    file.writelines(str_floats)

file_name_logs = f'log_{date.today()}.txt'
file_path_logs =  os.path.join('ml_projects', 'logs', file_name_logs)

with open(file_path_logs, 'w') as file:
    file.writelines(f"User: {name}\nDate: {date_now}\nData Points: {data_points}\nSum: {sum_of_r_float}\nAverage: {avg_of_r_float}\nSqrt of Average: {sqrt_of_r_float}")

print(f"Session logged for {name}")
print(f"Data saved to: {file_path_data}")
print(f"Log saved to: {file_path_logs}")