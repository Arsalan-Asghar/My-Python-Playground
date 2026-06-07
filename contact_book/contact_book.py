from abc import ABC, abstractmethod
import json
import csv
import os

class ContactBase(ABC):
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone
	@abstractmethod
	def get_info(self) -> str:
		pass
	@abstractmethod
	def get_type(self) -> str:
		pass

class PersonalContact(ContactBase):
	def get_info(self):
		return f'Name: {self.name}\nContact: {self.phone}'
	def get_type(self):
		return 'Contact Type: Personal'

class WorkContact(ContactBase):
	def __init__(self, name, phone, company):
		super().__init__(name, phone)
		self.company = company

	def get_info(self):
		return f'Name: {self.name}\nContact: {self.phone}\nCompany: {self.company}'

	def get_type(self):
		return 'Contact Type: Work Contact'

all_contacts = {}

def addContact(contacts):
	all_contacts[contacts.name] = contacts

def viewContact():
	if not all_contacts:
		print("No contact found.")
	else:
		for key, value in all_contacts.items():
			print(value.get_info())
			print(value.get_type())

def searchContact():
	ask = input("Enter the name of the contact you want to search: ")

	if ask not in all_contacts:
		print(f"No contact by the named {ask} found.")

	else:
		print(all_contacts[ask].get_info())

def deleteContact():
	print("Current list:")
	viewContact()
	ask = input("Enter the name of the contact you want to delete: ")

	if ask not in all_contacts:
		print(f"No contact by the named {ask} found.")
	else:
		del all_contacts[ask]
		print('Successfully done.')
		
		print("New list:")
		if not all_contacts:
			print("No contact")
		else:
			viewContact()

def saveToJSON():
	dic = {}
	for key, value in all_contacts.items():
		if hasattr(value, 'company'):
			dic[key] = {
			'Name': value.name,
			'Phone': value.phone,
			'Status': value.get_type(),
			'Company': value.company
			}
		else:
			dic[key] = {
		'Name': value.name,
		'Phone': value.phone,
		'Status': value.get_type()
		}

	with open('contacts.json', 'w') as f:
		json.dump(dic, f, indent=4)


def saveToCSV():
	file_e = os.path.exists('contacts.csv')
	with open('contacts.csv', 'a') as f:
		writer = csv.writer(f)
		if not file_e:
					writer.writerow(['Name', 'Phone', 'Status', 'Company'])
		for key,value in all_contacts.items(): 
			if hasattr(value, 'company'):
				writer.writerow([value.name, value.phone, value.get_type(), value.company])
			else:
				writer.writerow([value.name, value.phone, value.get_type(), ""])


def main():
	while True:
		try:
			print("\n--- Contact Book ---")
			print("1. Add Contact")
			print("2. View Contacts")
			print("3. Search Contact")
			print("4. Delete Contact")
			print("5. Save to JSON")
			print("6. Save to CSV")
			print("7. Exit")
			
			choice = input("Enter your choice: ")
			
			if choice == "1":
				c_name = input("Please enter the contact name: ")
				c_phone = input("Enter the contact number: ")
				c_type = input("""Is it Personal Contact ot Work Contact:
Press 1: Personal Contact
Press 2: Work Contact
Choose: """)
				if c_type == '1':
					p1 = PersonalContact(c_name, c_phone)
					addContact(p1)
					print("Successfully Added. ")
					print("---Contact List---")
					viewContact()

				elif c_type == '2':
					c_company = input("Please enter the name of the Company: ")
					w1 = WorkContact(c_name, c_phone, c_company)
					addContact(w1)
					print("Successfully Added. ")
					print("---Contact List---")
					viewContact()

				else:
					print("Please choose from the options")
					continue


			elif choice == "2":
				viewContact()

			elif choice == "3":
				searchContact()
				
			elif choice == "4":
				deleteContact()
				
			elif choice == "5":
				saveToJSON()
			
			elif choice == "6":
				saveToCSV()

			elif choice == "7":
				print("Goodbye!")
				break
			else:
				print("Invalid choice.")
		except ValueError:
			print("Please enter a correct value.")

if __name__=='__main__':
	main()