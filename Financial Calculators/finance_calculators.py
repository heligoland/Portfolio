"""
===============================================================
Financial Calculators Module
---------------------------------------------------------------
File:     finance_calculators.py
Version:  1.2
Date:     07/12/2025
Author: Annelli

Description:
    This module provides two command‑line financial calculators:
    
    1. Investment Calculator
       - Computes Return on Investment (ROI) using either
         simple or compound interest.
       - Supports monthly or yearly compounding.

    2. Bond Repayment Calculator
       - Calculates monthly repayments on a home loan (bond)
         based on principal, interest rate, and repayment period.

Features:
    - Robust input validation for numeric and choice-based inputs.
    - Clear user prompts and error handling.
    - Uses standard financial formulas for accuracy.

Intended Use:
    Run this script in a terminal or command prompt.
    The user will be guided interactively through all inputs.

Dependencies:
    - Python 3.x
    - math (standard library)

License:
    This script is provided for educational and practical use.
    Modify or extend as needed for your financial applications.
===============================================================
"""

import math

# -------------------------------------------------------------
# Helper functions for safe input
# -------------------------------------------------------------
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a numeric value.")
            
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter an integer value.")
            
def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().casefold().capitalize()
        if choice in valid_choices:
            return choice
        else:
            print(f"Error: Please enter one of {valid_choices}.")


# -------------------------------------------------------------
# Display menu
# -------------------------------------------------------------
print("""
Investment calculator: to calculate your ROI
Bond calculator: to calculate the monthly repayment on your bond
""")

# -------------------------------------------------------------
# Main loop for calculator type
# -------------------------------------------------------------
user_input = get_choice("Enter either 'Investment' or 'Bond' from the menu above to proceed: \n", ["Investment", "Bond"])


# -----------------------------
# Investment calculator
# -----------------------------
if user_input == "Investment":
    principal = get_float("\nEnter the principal investment amount (R): \n")
    rate_input = get_float("\nEnter the rate of interest (%): \n")
    period = get_int("\nEnter the total investment period (years): \n")
    interest_type = get_choice("\nEnter 'Simple' or 'Compound' to choose your interest type: \n", ["Simple", "Compound"])
    
    rate = rate_input / 100
    
    # -----------------------------
    # Simple interest calculation
    # -----------------------------
    if interest_type == "Simple":
        simple_roi = principal * (1 + (rate * period))
        print(f"\nYour total ROI after {period} years will be: R{simple_roi:.2f}")
    
    # -----------------------------
    # Compound interest calculation
    # -----------------------------
    else: # Compound
        compound_frequency = get_choice("\nShould the interest be monthly or yearly compounding? Enter 'Monthly' or 'Yearly' to select your choice: \n", ["Monthly", "Yearly"])
        
        if compound_frequency == "Monthly": # Monthly compounding
            compound_roi = principal * math.pow((1 + (rate / 12)),(12 * period))
        
        else: # Yearly compounding
            compound_roi = principal * math.pow((1 + rate), period)
        
        print(f"\nYour total ROI after {period} years will be: R{compound_roi:.2f}")


# -----------------------------
# Bond calculator
# -----------------------------
elif user_input == "Bond":
    principal = get_float("\nEnter the bond principal amount (R): \n")
    rate = get_float("\nEnter the rate of interest (%): \n")
    period_type = get_choice("\nWould you like your bond period to be defined in 'Years' or 'Months': \n", ["Years", "Months"])
    
    # -----------------------------
    # User defined Period in Years
    # -----------------------------
    if period_type == "Years": 
        period_years = get_int("\nEnter the total bond period (Years): \n")
        period = period_years * 12 # Convert to Months
    
    # -----------------------------
    # User defined Period in Months
    # -----------------------------
    else:
        period = get_int("\nEnter the total bond period (Months): \n")

    monthly_rate = (rate / 100) / 12
    monthly_repayment = (monthly_rate * principal) / (1 - (1 + monthly_rate)**(-period))

    print(f"\nYour total monthly repayment will be: R{monthly_repayment:.2f}")


# ----------------------- END OF CODE -------------------------
