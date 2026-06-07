import json
import os

def addData():
    name = input("Please enter the name: ")
    while True:
        try:
            age = int(input("Please enter the age: "))
            break
        except ValueError:
            print('Please enter a number as age (e.g 21)')

    city = input("Please enter your city name: ")
    country = input("Please enter your country name: ")

    new_data = {
        'name': name,
        'age': age,
        'address':{
            'city': city,
            'country': country
            }
        }

    if os.path.exists("info.json"):
        with open("info.json", "r") as f:
            data = json.load(f)  # load existing list
    else:
        data = []  # start fresh

    data.append(new_data)  # add new person

    with open ('info.json', 'w') as f:
        json.dump(data, f, indent=4)

        print('Successfully added!')

def viewData():
    print("*"*10)
    print("Your Data:")
    print("*"*10)

    try:
        with open('info.json', 'r') as f:
            read = json.load(f)

            if not read:
                print("Nothing in it.")
            else:
                for person in read:
                    for key, value in person.items():
                        if isinstance(value, dict):
                            print(f'{key}')
                            for k, v in value.items():
                                print(f"    {k}: {v}")
                        else:
                            print(f"{key}: {value}")
    except FileNotFoundError:
        print("There is no file to view.")

def main():
    while True: 
        choose = input("""Please choose the option you want to perform:
    1. Save data as JSON:
    2. View saved data:
    3. Exit

    Choose (1,2 or 3):  """)

        if choose == '1':
            addData()
        elif choose == '2':
            viewData()
        elif choose == '3':
            print("Thanks for using. GoodBye!")
            break
        else:
            print('Please choose from the given options.')

        ask = input("Do you want to perfrom any task again? (Y/n):  ").lower()
        if ask == 'n':
            print('GoodBye')
            break
        else:
            continue

if __name__ == '__main__':
    main()