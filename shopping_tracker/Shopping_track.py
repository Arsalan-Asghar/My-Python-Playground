import csv

def shopping_list():
    budget = float(input("Enter your budget: "))
    shopping_items = {}

    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == "done":
            break

        price = float(input(f"Enter price of {item}: "))
        shopping_items[item] = price

    with open("shopping_list.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Budget", budget])
        writer.writerow(["Item", "Price"])
        for item, price in shopping_items.items():
            writer.writerow([item, price])

    total_cost = sum(shopping_items.values())
    left = budget - total_cost
    print(f"\nTotal cost: Rs {total_cost:.2f}")
    if total_cost < budget:
        print(f"You saved some money\nBudget left: Rs {left:.2f}")
    elif total_cost == budget:
        print(f"You used your whole budget.")
    else:
        print(f"You have exceeded your budget by: Rs {abs(left)}")
    print("Your shopping list has been saved to shopping_list.csv")

if __name__=='__main__':
    shopping_list()
    