"""
===========================================================
 NIKE WAREHOUSE STOCK MANAGEMENT SYSTEM
-----------------------------------------------------------
 File:    inventory.py
 Version: 1.1
 Date:    24/12/2025
 Author:  Annelli
 
 Description:
     This program manages stock-taking for a Nike warehouse.
     It reads shoe inventory data from a text file, stores it
     as objects, and allows the user to:

        • View all shoes
        • Add new shoes
        • Restock the lowest‑quantity item
        • Search for a shoe by code
        • Calculate total value per item
        • Display the highest‑quantity item (for sale)

     The program demonstrates object‑oriented programming,
     file handling, defensive coding, and modular design.

Notes: 
    This program is intended for educational purposes to
    illustrate recursion, not for performance‑critical use.
===========================================================
"""

from dataclasses import dataclass
from tabulate import tabulate
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "inventory.txt")


# ---------------------------------------------------------
# The beginning of the class
# ---------------------------------------------------------
@dataclass
class Shoe:
    """
    A class representing a shoe item in the warehouse.
    """
    country: str
    code: str
    product: str
    cost: int
    quantity: int

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"Country: {self.country} | Code: {self.code} | "
                f"Product: {self.product} | Cost: {self.cost} | "
                f"Quantity: {self.quantity}")


# ---------------------------------------------------------
# Shoe list
# ---------------------------------------------------------
# This list stores all Shoe objects created from the inventory file.
shoe_list = []


# ---------------------------------------------------------
# Functions outside the class
# ---------------------------------------------------------
def read_shoes_data():
    """
    Read shoe data from inventory.txt and populate shoe_list.
    Uses try/except for defensive error handling.
    """
    try:
        with open(file_path, "r") as file:
            next(file)  # Skip header line

            for line in file:
                if line.strip() == "":
                    continue  # Skip empty lines

                # Split CSV line into components
                country, code, product, cost, quantity = line.strip().split(",")

                # Create Shoe object and store it
                shoe = Shoe(country, code, product, int(cost), int(quantity))
                shoe_list.append(shoe)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def capture_shoes():
    """
    Allow the user to manually enter a new shoe item.
    Creates a Shoe object and appends it to shoe_list.
    """
    try:
        country = input("Enter country: ")
        code = input("Enter product code: ")
        product = input("Enter product name: ")
        cost = int(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        new_shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(new_shoe)

        update_inventory_file()

        print("Shoe added successfully.")

    except ValueError:
        print("Invalid input. Cost and quantity must be numbers.")


def view_all():
    """
    Display all shoes in the shoe_list in a formatted table.
    """
    if not shoe_list:
        print("No shoes loaded.")
        return

    print("\n===== ALL SHOES =====")
    print(tabulate(shoe_list, headers="keys", tablefmt="fancy_grid"))
    print()


def re_stock():
    """
    Find the shoe with the lowest quantity and offer to restock it.
    Updates the inventory file after restocking.
    """
    if not shoe_list:
        print("No shoes loaded.")
        return

    # Find shoe with lowest quantity
    lowest = min(shoe_list, key=lambda s: s.quantity)

    print("\n===== LOWEST STOCK ITEM =====")
    print(tabulate([lowest], headers="keys", tablefmt="fancy_grid"))
    print()

    # Ask user if they want to restock
    choice = input("Do you want to restock this item? (yes/no): ").lower()

    if choice == "yes":
        try:
            add_qty = int(input("Enter quantity to add: "))
            lowest.quantity += add_qty

            update_inventory_file()
            print("Stock updated successfully.")

        except ValueError:
            print("Invalid quantity entered.")


def search_shoe():
    """
    Search for a shoe by its code and print the result.
    """
    code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("\n===== SHOE FOUND =====")
            print(tabulate([shoe], headers="keys", tablefmt="fancy_grid"))
            print()
            return shoe

    print("No shoe found with that code.")
    return None


def value_per_item():
    """
    Calculate and display the total value of each shoe.
    Formula: value = cost * quantity
    """
    if not shoe_list:
        print("No shoes loaded.")
        return

    table = []
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        table.append([
            shoe.product,
            shoe.code,
            shoe.cost,
            shoe.quantity,
            value
        ])

    print("\n===== VALUE PER ITEM =====")
    print(tabulate(
        table,
        headers=["Product", "Code", "Cost", "Qty", "Total Value"],
        tablefmt="fancy_grid"
    ))
    print()


def highest_qty():
    """
    Display the shoe with the highest quantity.
    """
    if not shoe_list:
        print("No shoes loaded.")
        return

    highest = max(shoe_list, key=lambda s: s.quantity)

    print("\n===== PRODUCT FOR SALE =====")
    print(tabulate([highest], headers="keys", tablefmt="fancy_grid"))
    print()


def update_inventory_file():
    """
    Rewrite inventory.txt with updated shoe quantities.
    Ensures file stays in sync with shoe_list.
    """
    lines = ["Country,Code,Product,Cost,Quantity"]
    for shoe in shoe_list:
        lines.append(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

    with open(file_path, "w") as file:
        file.write("\n".join(lines))

# ---------------------------------------------------------
# Main Menu
# ---------------------------------------------------------
def main():
    """
    Display the main menu and execute user-selected actions.
    Runs inside a loop until the user chooses to exit.
    """
    read_shoes_data()

    while True:
        print("""
========= NIKE WAREHOUSE MENU =========
1 - View all shoes
2 - Add new shoe
3 - Restock lowest quantity
4 - Search shoe by code
5 - View value per item
6 - Show highest quantity (for sale)
7 - Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

# --------------------- End of Code -----------------------
