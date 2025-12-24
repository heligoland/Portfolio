"""
===========================================================
Recursive Maximum Finder
-----------------------------------------------------------
 File:    largest_number.py
 Version: 1.0
 Date:    22/12/2025
 Author:  Annelli

 Description:
     This program defines a recursive function that determines
     the largest number in a list without using loops or the
     built-in max() function. The algorithm works by comparing
     the first element of the list with the largest element in
     the remainder of the list, reducing the problem size on
     each recursive call.

     The recursion terminates when the list contains only one
     element, which is returned as the base case.

 Requirements:
     • Python 3.x
     • No external libraries required

 Usage Example:
     numbers = [3, 1, 6, 8, 2, 4, 5]
     result = largest_number(numbers)
     print(result)   # Output: 8

 Notes:
     • Includes input validation to ensure safe execution.
     • Optional tracing output is included to visualise the
       recursive call sequence.
     • This function is intended for educational purposes to
       illustrate recursion.
===========================================================
"""

# =========================================================
# PSEUDOCODE
# =========================================================
# function largest_number(list):
#     if list has length 1:
#         return list[0]
#    else:
#         largest_rest = largest_number(list[1:])
#        
#         if list[0] > largest_rest:
#             return list[0]
#         else:
#             return largest_rest

# =========================================================
# PYTHON CODE
# =========================================================

# ---------------------------------------------------------
# Recursive function including input validation and print-tracing
# ---------------------------------------------------------

def largest_number(numbers_list):
    """
    Recursively finds the largest number in a list.
    """

    # -----------------------------
    # Input validation
    # -----------------------------
    if not isinstance(numbers_list, list):
        raise TypeError("Input must be a list.")

    if len(numbers_list) == 0:
        raise ValueError("List cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in numbers_list):
        raise ValueError("All elements in the list must be numbers.")

    # -----------------------------
    # Recursion tracing
    # -----------------------------
    print(f"Calling largest_number on: {numbers_list}")

    # -----------------------------
    # Base case
    # -----------------------------
    if len(numbers_list) == 1:
        print(f"Base case reached: returning {numbers_list[0]}")
        return numbers_list[0]

    # -----------------------------
    # Recursive case
    # -----------------------------
    largest_rest = largest_number(numbers_list[1:])

    # Compare first element with the largest of the rest
    if numbers_list[0] > largest_rest:
        print(f"Comparing {numbers_list[0]} with {largest_rest} → keeping {numbers_list[0]}")
        return numbers_list[0]
    else:
        print(f"Comparing {numbers_list[0]} with {largest_rest} → keeping {largest_rest}")
        return largest_rest

# Example test
print("Largest number in", [5, 6, 18, 24, 2, 30, 16, 58], ":", largest_number([5, 6, 18, 24, 2, 30, 16, 58]))

# ============== END OF CODE ==============
