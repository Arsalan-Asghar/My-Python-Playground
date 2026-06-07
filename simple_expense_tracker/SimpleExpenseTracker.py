################# Simple Expense Tracker ####################
import csv
import os

def addExp():
	while True:
		DateTime = input("Please enter the date (DD/MM/YYYY): ")
		item = input("Please enter the item name: ")	
		try:
			amount = int(input("Please enter the amount: "))
		except ValueError:
			print("Please enter a number.")
			continue

		file_exist = os.path.exists("exp.csv")

		with open("exp.csv", "a") as f:
			writer =  csv.writer(f)
			if not file_exist:
				writer.writerow(['Date', 'Item', 'Amount'])
			writer.writerow([DateTime, item, amount])
			break

	print("DONE!")


def viewExp():
	try:
		with open("exp.csv", "r") as f:
			reading = csv.reader(f)
			next(reading)
			rows = list(reading)
			if not rows:
				print("Empty")
			else:
				print("-" * 40)
				print(f"{'Date':<15} {'Item':<15} {'Amount'}")
				print("-" * 40)
				for row in rows:
					print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15}\n")				
	except FileNotFoundError:
		print("There is no file to read")


def main():
	while True:
		choice = input("""What do you want to perform?
1. Add an Expense: 
2. View Expenses:
3. Exit

Choose (1,2,3):	""")

		match choice:

			case '1':
				addExp()
			case '2':
				viewExp()
			case '3':
				print("Thanks for using. Goodbye!")
				break
			case _:
				print("Please enter a correct choice")
				
		ask = input("Do you want to perfrom any action again? (y/N):	").lower()
		if ask == 'y':
			continue
		else:
			print("Goodbye")
			break

if __name__ == "__main__":
	main()