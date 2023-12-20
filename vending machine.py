from rich import print as rprint
from rich.text import Text
from rich.console import Console
from rich.table import Table
import time
import sys
import time
from rich.progress import Progress
from rich import print
from rich.layout import Layout


# Title
title = Text('''
▀█░█▀ █▀▀ █▀▀▄ █▀▀▄ ░▀░ █▀▀▄ █▀▀▀ 　 █▀▄▀█ █▀▀█ █▀▀ █░░█ ░▀░ █▀▀▄ █▀▀ █ 
░█▄█░ █▀▀ █░░█ █░░█ ▀█▀ █░░█ █░▀█ 　 █░▀░█ █▄▄█ █░░ █▀▀█ ▀█▀ █░░█ █▀▀ ▀ 
░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░░▀ ▀▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀ ▄
           ''', justify="center", style="cyan")
console = Console()
console.print(title, justify="center")

# Table 1 title
table = Table(title="\nChoose your drink/s:")
# Drinks columns 
table.add_column("Code", justify="right", style="cyan", no_wrap=True)
table.add_column("Drink", style="magenta")
table.add_column("Price", justify="right", style="green")
table.add_column("Stock", justify="center", style="yellow")

# Table 1: Drinks
drinks = [
    {"code": "D1", "name": "Water", "price": 1.50, "stock": 10},
    {"code": "D2", "name": "Iced Coffee", "price": 7.00, "stock": 10},
    {"code": "D3", "name": "C2 Iced Tea", "price": 4.00, "stock": 10},
    {"code": "D4", "name": "Mogu Mogu", "price": 4.00, "stock": 10},
    {"code": "D5", "name": "Milk Tea","price":10.00,"stock":10}
]

for drink in drinks:
    table.add_row(drink["code"], drink["name"], f"AED {drink['price']}", str(drink["stock"]))

# Print table 1
console = Console()
console.print(table, justify="center")

# Table 2 title
table2 = Table(title="\nChoose your snack/s:")
# Snacks columns 
table2.add_column("Code", justify="center", style="cyan", no_wrap=True)
table2.add_column("Snack", style="magenta")
table2.add_column("Price", justify="center", style="green")
table2.add_column("Stock", justify="center", style="yellow")

# Table 2: Snacks
snacks = [
    {"code": "S1", "name": "Chicharon ni Mang Juan", "price": 5.00, "stock": 10},
    {"code": "S2", "name": "DingDong", "price": 5.00, "stock": 10},
    {"code": "S3", "name": "Piattos", "price": 5.00, "stock": 10},
    # Add more snacks as needed
]

for snack in snacks:
    table2.add_row(snack["code"], snack["name"], f"AED {snack['price']}", str(snack["stock"]))

# Print table 2
console = Console()
console.print(table2, justify="center")

line_break = "\n+============== Enter Code (type 'quit' if you're good to go): ===============+"
console.print(line_break, justify="center")


def get_user_choice():
    user_choice = input("\nEnter:".center(164))
    return user_choice.strip()

def product_choice(choice, products):
    for product in products:
        if choice == "quit":
            return None
        elif choice == product["code"]:
            if product["stock"] > 0:
                product["stock"] -= 1  # Decrease the stock when a product is selected
                return product
            else:
                print(f"Sorry, {product['name']} is out of stock.")
                return None
    else:
        print("Invalid Input")
        return None

def confirm_quit():
    confirmation = input("\nAre you sure you want to quit? (yes/no): ").lower()
    return confirmation

       

selected_products = []

while True:
    choice = get_user_choice()

    # Check if the choice is 'quit'
    if choice.lower() == "quit":
        confirmation = confirm_quit()

        if confirmation != "yes" or confirmation != "y":
            break  # Exit the loop immediately if the user confirms quitting
        else:
            continue

    product = product_choice(choice, drinks + snacks)

    if product is not None:
        selected_products.append(product)
        print(f"{product['name']}: is added to your basket. Remaining stock: {product['stock']}")
    else:
        break

# Function to calculate total
def calculate_total(selected_products):
    total = sum(product["price"] for product in selected_products)
    return total

while True:
    choice = get_user_choice()
    product = product_choice(choice, drinks + snacks)

    if product is not None:
        selected_products.append(product)
        print(f"{product['name']}: is added to your basket. Remaining stock: {product['stock']}")
    else:
        break

#Dispaying the order
if selected_products:
    table3 = Table(title="\nYour Order:")
# Order columns
table3.add_column("Product", justify="center", style="cyan", no_wrap=True)
table3.add_column("Price", justify="center", style="cyan", no_wrap=True)

# Add rows to the table
for product in selected_products:
    table3.add_row(f"{product['name']}", f"AED {product['price']}")

console = Console()
console.print(table3, justify="center")

# Display total
total = calculate_total(selected_products)
print("\n Total:".center(70))
print(f"AED {total}".center(70))

# Tiny animation to show it's done
animation = "|/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.2)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 3:  # The animation will last for 3 seconds
        break
line_break1 = "\n+======================== Payment: Input the Amount ==========================+"
console.print(line_break1,justify="center")    


total = calculate_total(selected_products)
total = int(total)

while True:
    payment = input("\nInput:".center(164))

    try:
        # Convert payment to an integer
        payment = int(payment)

        change = payment - total

        if payment >= total:
            print(f"\nChange: AED {change}".center(70))
            with Progress() as progress:
              task1 = progress.add_task("[white]Dispensing", total=100)
              while not progress.finished:
                 progress.update(task1, advance=0.9)
                 time.sleep(0.02)
            print("Your Order has been dispensed.")

            break  # Exit the loop if payment is sufficient
        else:
            print("Your payment is insufficient. Try Again")
            print(f"Payment: AED {payment}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


#####################
