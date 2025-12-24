# ============= Program to calculate BMI =============

# Helper function to ensure valid input

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI) given weight in kg and height in meters."""
    try:
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi = height / (weight ** 2) # I purposefully swapped around weight and height to demonstrate a logical error.
        return bmi
    except TypeError:
        print("Invalid input type. Please provide numeric values for weight and height.")
        return None
    except ValueError as ve:
        print(ve)
        return None
    
''' # Example usage

weight = 70  # in kilograms
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
    
if bmi is not None:
    print(f"Your BMI is: {bmi:.2f}")
'''
''' # Test with invalid inputs

invalid_weight = "seventy"
invalid_height = 0
calculate_bmi(invalid_weight, height)
calculate_bmi(weight, invalid_height)
'''

# Main program to get user input and display BMI
print("Welcome to the BMI Calculator!\n")

weight = float(input("Please enter your weight in kg: \n"))
height = float(input("\nPlease enter your height in meters: \n"))

bmi = calculate_bmi(weight, height)
    
if bmi is not None:
    print(f"Your BMI is: {bmi:.2f}")

# =================== END OF CODE ===================
