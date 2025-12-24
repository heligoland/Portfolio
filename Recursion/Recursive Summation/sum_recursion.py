"""
===========================================================
Recursive Summation
-----------------------------------------------------------
 File:    sum_recursion.py
 Version: 1.0
 Date:    22-12-2025
 Author:  Annelli

 Description:
     This program defines a recursive function that calculates
     the sum of all numbers in a list from index 0 up to a
     specified index. It demonstrates the two essential parts
     of recursion: a base case and a recursive step.

     The function repeatedly calls itself, reducing the index
     by one each time, until it reaches the base case at index 0.
     This mirrors the mathematical recurrence:

         S(n) = list[n] + S(n - 1)

 Requirements:
     • Python 3.x
     • No external libraries required

 Usage Example:
     numbers = [1, 3, 6, 2, 14, 26]
     result = adding_up_to(numbers, 5)
     print(result)   # Output: 52

 Notes:
     • Includes input validation to ensure safe execution.
     • Optional tracing output can be enabled to visualise
       the recursive call sequence.
     • This function is intended for educational purposes to
       illustrate recursion, not for performance‑critical use.
===========================================================
"""

# =========================================================
# PSEUDOCODE
# =========================================================
# function adding_up_to(numbers_list, index):
#
#     if index == 0:
#         return numbers_list[0]
#
#     else:
#         sum_rest = adding_up_to(numbers_list, index - 1)
#         return numbers_list[index] + sum_rest


# =========================================================
# PYTHON CODE
# =========================================================

# ---------------------------------------------------------
# Recursive function including input validation and print-tracing
# ---------------------------------------------------------
def adding_up_to(numbers_list, index):
    """
    Recursively sums all elements in numbers_list from index 0 up to the given index.
    """

    # -----------------------------
    # Input validation
    # -----------------------------
    if not isinstance(numbers_list, list):
        raise TypeError("numbers_list must be a list.")

    if not all(isinstance(x, (int, float)) for x in numbers_list):
        raise ValueError("All elements in numbers_list must be numbers.")

    if not isinstance(index, int):
        raise TypeError("index must be an integer.")

    if index < 0:
        raise ValueError("index cannot be negative.")

    if index >= len(numbers_list):
        raise IndexError("index is out of range for the list.")

    # -----------------------------
    # Recursion tracing
    # -----------------------------
    print(f"Calling adding_up_to with index = {index}")

    # -----------------------------
    # Base case
    # -----------------------------
    if index == 0:
        print(f"Base case reached: returning {numbers_list[0]}")
        return numbers_list[0]

    # -----------------------------
    # Recursive case
    # -----------------------------
    result = numbers_list[index] + adding_up_to(numbers_list, index - 1)
    print(f"Returning {numbers_list[index]} + sum_up_to({index - 1}) = {result}")
    return result


# Example test
print("\nFinal result:", adding_up_to([1, 3, 6, 2, 14, 26], 5))

# ============= END OF CODE =============
