## Hello
## P.S. I've pushed it but it's still in progress :))

# Importing necessary libraries
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
from rich.panel import Panel


# Vending Machine title
title = Text('''
▀█░█▀ █▀▀ █▀▀▄ █▀▀▄ ░▀░ █▀▀▄ █▀▀▀ 　 █▀▄▀█ █▀▀█ █▀▀ █░░█ ░▀░ █▀▀▄ █▀▀ █ 
░█▄█░ █▀▀ █░░█ █░░█ ▀█▀ █░░█ █░▀█ 　 █░▀░█ █▄▄█ █░░ █▀▀█ ▀█▀ █░░█ █▀▀ ▀ 
░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░░▀ ▀▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀ ▄
           ''', justify="center", style="#FFDF00")
console = Console()
console.print(title, justify="center")

# A small description about the vending machine 
intro_msg = """
     Hey there! This vending machine offers some Asian drinks and snacks 
that you may or may have heard of. Craving for a new taste? Give it a go :)) !!
"""
intro_panel = Panel(intro_msg, style="yellow")
console.print(intro_panel, justify = "center")

#========================================================== TABLE 1 DRINKS ====================================================================

table = Table(title="\nChoose your drink/s:") # title

# Table 1: Drink Columns and how it's styled
table.add_column("Code", justify="right", style="cyan", no_wrap=True)
table.add_column("Drink", style="magenta")
table.add_column("Price", justify="right", style="green")
table.add_column("Stock", justify="center", style="yellow")

# Table 1: Selection of Drinks
drinks = [
    {"code": "D1", "name": "Water", "price": 1.50, "stock": 10},
    {"code": "D2", "name": "Iced Coffee", "price": 7.00, "stock": 10},
    {"code": "D3", "name": "C2 Iced Tea", "price": 4.00, "stock": 10},
    {"code": "D4", "name": "Mogu Mogu", "price": 4.00, "stock": 10},
    {"code": "D5", "name": "Milk Tea","price":10.00,"stock":10},
    {"code": "D6", "name": "Schweppes Ginger Ale","price":3.50,"stock":10},
    {"code": "D7", "name": "Soju in Botte","price":15.00,"stock":10},
    {"code": "D8", "name": "Apple Juice","price":3.50,"stock":10},
    {"code": "D9", "name": "Orange Juice","price":3.50,"stock":10},
]
# loop to iterate the drinks(including code, price and stock) in the dictionary
for drink in drinks:
    table.add_row(drink["code"], drink["name"], f"AED {drink['price']}", str(drink["stock"]))
# Finally printing TABLE 1
def drinks_table1():
    console = Console()
    console.print(table, justify="center")

#calling the function
drinks_table1()

#========================================================== TABLE 2 SNACKS =================================================================

table2 = Table(title="\nChoose your snack/s:") #title
# Table 2: Snack Columns and how it's styled
table2.add_column("Code", justify="center", style="cyan", no_wrap=True)
table2.add_column("Snack", style="magenta")
table2.add_column("About", justify="center")
table2.add_column("Price", justify="center", style="green")
table2.add_column("Stock", justify="center", style="yellow")

# Table 2: Selection of Snacks
snacks = [
    {"code": "S1", "name": "Chicharon","about":"Fried Chicken skin","price": 5.00, "stock": 10},
    {"code": "S2", "name": "Choco Pie 1-pack","about":"Chocolate-covered marshmallow sandwich", "price": 4.00, "stock": 10},
    {"code": "S3", "name": "Piattos","about":"Potato crisps in cheese flavor", "price": 5.00, "stock": 10},
    {"code": "S4", "name": "Dried Seaweed","about":"Sheets of Dried seaweed", "price": 6.00, "stock": 10},
    {"code": "S5", "name": "Taiyaki","about":"Fish-shaped pastry with sweet fillings", "price": 5.00, "stock": 10},
    {"code": "S6", "name": "Chippy","about":"Crispy corn chips", "price": 5.00, "stock": 10},
    {"code": "S7", "name": "Oishi Potato Fries","about":"Seasoned potato fries", "price": 5.00, "stock": 10},
    {"code": "S8", "name": "LaLa Fish Crackers","about":"Fish flavored crackers", "price": 5.00, "stock": 10},
    {"code": "S9", "name": "Boy Bawang","about":"Garlic-flavored corn nuts", "price": 5.00, "stock": 10},
    {"code": "S10", "name": "Cheese Rings","about":"Cheesy, crispy rings :)", "price": 5.00, "stock": 10},
]
# loop to iterate the snacks(including code, about, price and stock) in the dictionary
for snack in snacks:
    table2.add_row(snack["code"], snack["name"], snack['about'],f"AED {snack['price']}", str(snack["stock"]))
# Print table 2
def snacks_table2():
    console = Console()
    console.print(table2, justify="center")

#calling the function
snacks_table2()

#======================================= Selection of Product // Ordering ========================================

# Instruction in a 'yellow' panel to enter code/quit
enter_panel = Panel('''\n[bold yellow]Enter Code (type 'quit' if you're good to go):    [reset]
                   ''', style="yellow") 
console.print(enter_panel, justify="center") # to print

# function to store user's input
def get_user_choice():
    user_choice = input("\nEnter:".center(164))
    return user_choice.strip()

# function: quit confirmation
def confirm_quit():
    confirmation = input("\nAre you sure you want to quit? (yes/no): ").lower()
    return confirmation

# function with choice, products argument 
def product_choice(choice, products):
    # if users input quit, it would return no value 
    for product in products:
        if choice == "quit":
            return None
    # if users input a code, the value would be stored
        elif choice == product["code"]:
            if product["stock"] > 0:
                product["stock"] -= 1  # It would decrease the stock when a product is selected
                return product
            else:
                # It would also announce when the product runs out
                console.print(Panel(f"Sorry, {product['name']} is out of stock."), style="#141C3B", justify="center")
                confirmation = confirm_quit()
                print(confirmation)
                if confirmation == "no" or confirmation == "n":
                          get_user_choice()
            return None
    
    else:
        print("Invalid Input")
        return None
        

# empty list for selected products
selected_products = []

while True:
    choice = get_user_choice()

    # Check if the choice is 'quit'
    if choice.lower() == "quit":

        confirmation = confirm_quit()
        if confirmation == "yes" or confirmation == "y":
            break  # Exit the loop immediately if the user confirms quitting

    # Getting the users product choice to add it on the list and print the remaining stock
    product = product_choice(choice, drinks + snacks)
    if product is not None:
        selected_products.append(product)
        print(f"{product['name']}: is added to your basket. Remaining stock: {product['stock']}")
    else:
        continue  # Continue to the next iteration if the product choice is invalid

# Function: The sum of selected product prices
def calculate_total(selected_products):
    total = sum(product["price"] for product in selected_products)
    return total

#============================================ Suggestion System ========================================================

def suggest_purchase(selected_products, drinks, snacks):
    # Extract the types of products (drinks and snacks) the user has selected
    selected_drinks = [product["name"] for product in selected_products if product in drinks]
    selected_snacks = [product["name"] for product in selected_products if product in snacks]

    # Create a list to store suggested products
    suggestions = []

    # Check for suggestions based on selected products
    if "Iced Coffee" in selected_drinks:
        # Suggest a snack that goes well with iced coffee
        snack_suggestion = {"name": "Choco Pie 1-pack", "price": 4.00, "stock": 10}
        suggestions.append(snack_suggestion)

    if "Mogu Mogu" in selected_drinks:
        # Suggest a snack that goes well with iced coffee
        snack_suggestion = {"name": "Taiyaki", "price": 5.00, "stock": 10}
        suggestions.append(snack_suggestion)

    if "Taiyaki" in selected_snacks:
        # Suggest a snack that goes well with iced coffee
        snack_suggestion = {"name": "MilkTea", "price": 5.00, "stock": 10}
        suggestions.append(snack_suggestion)

    # You can add more conditions and suggestions based on your specific criteria

    return suggestions

# Call the suggestion function
purchase_suggestions = suggest_purchase(selected_products, drinks, snacks)

# Display the suggestions
if purchase_suggestions:
    titlesuggest= Panel((f'''[bold yellow]Your order would really go well with[reset]'''), style="#141C3B")
    console.print(titlesuggest, justify="center")
    for suggestion in purchase_suggestions:
        suggest_panel= Panel((f'''[bold cyan] {suggestion['name']} - AED {suggestion['price']} !![reset]'''), style="#141C3B")
        console.print(suggest_panel, justify="center")
else:
    nosuggest_panel= Panel((f"There's no suggestion at the moment :)"), style="#141C3B")
    console.print(nosuggest_panel, justify="center")

# ================================= TABLE 3 : Displaying the ORDER RECEIPT =========================

if selected_products:
    table3 = Table(title="\nYour Order:")
    # Order columns: Product and its price
    table3.add_column("Product", justify="center", style="cyan", no_wrap=True)
    table3.add_column("Price", justify="center", style="cyan", no_wrap=True)

    # the selected products and its price in rows
    for product in selected_products:
        table3.add_row(f"{product['name']}", f"AED {product['price']}")
    
    # Print table 3
    console = Console()
    console.print(table3, justify="center")

    # Calculating the TOTAL AMOUNT
    total = calculate_total(selected_products)  # calculate_amount function
    linebreak3 = Panel(f"[bold green]TOTAL: AED {total}[reset]", style="#141C3B")
    console.print(linebreak3, justify="center")

    # Storing the value in total 
    total = calculate_total(selected_products)
    total = int(total)
    remaining_payment = total 

    # while the remaining amount isn't totally paid yet, it will ask for an input
    while remaining_payment > 0: 
        if confirmation == 'yes':

# =============================================================== ACQUIRING THE PAYMENT =========================================================
            
            linebreak = ('''\n+==============================================================================+''')
            console.print(linebreak, justify="center") 

            # Small message 
            almost_msg = Panel(f'''\n[bold yellow]You're almost there![bold magenta] Proceeding to Payment...[reset][reset]''', style="#141C3B")
            console.print(almost_msg, justify="center")

            # Instruction in a panel to insert payment
            line_break2 = Panel('''\n[bold green] INSERT PAYMENT    [reset]
                           ''', style="green")
            console.print(line_break2, justify="center")

            while True:
                payment = input("\nInput:".center(164))

                try:
                    # Convert payment to an integer
                    payment = int(payment)

                    # Ensure the payment is positive
                    if payment > 0:
                        remaining_payment -= payment

                        if remaining_payment <= 0:
                            # If the total payment is sufficient or more, proceed to dispense the product
                            change = abs(remaining_payment)  # Calculate change
                            change_panel = Panel(f'''\n[bold yellow]CHANGE: AED {change}[reset]''', style="#141C3B")
                            console.print(change_panel, justify="center")

                            # An animatic progress bar to showcase your product is being dispensed
                            with Progress(console=console, transient=True) as progress:
                                task1 = progress.add_task("[white]Dispensing", total=100)

                                while not progress.finished:
                                    progress.update(task1, advance=0.9)
                                    progress.refresh()
                                    time.sleep(0.02)

#=============================================================== ORDER HAS BEEN DISPENSED ========================================================

                            linebreak = ('''\n+==============================================================================+''')
                            console.print(linebreak, justify="center") 

                            # A message that the order has been dispensed
                            dispensed_msg = Panel(f'''\n[bold yellow]Great! Your Order has been [bold magenta] DISPENSED.[reset][reset]''', style="#141C3B")
                            console.print(dispensed_msg, justify="center")

                            # A little thank you message :))
                            thankyou = Panel('''\n[bold green]THANK YOU FOR PURCHASING ! SEE YOU AGAIN :)   [reset]
                               ''', style="green")
                            console.print(thankyou, justify="center")

                            break
                        else:
                            print(f"Remaining amount to pay: AED {remaining_payment}")
                            # the message to display the remaining amount to pay left
                    else:  # alerts when input is invalid e.g. negative values and non-numeric values
                        print("Invalid input. Please enter a positive numeric value.") 
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value.")
        else:
            break  # exit the loop if confirmation is not 'yes'

