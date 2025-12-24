"""
===========================================================
 Holiday Cost Calculator
-----------------------------------------------------------
 File: holiday.py
 Version: 1.1
 Date: 24/12/2024
 Author: Annelli
 
 Description:
     A simple command-line application that calculates the
     total cost of a holiday based on:
         • Destination city (validated)
         • Number of hotel nights
         • Car rental duration
     Includes defensive programming and input validation to
     ensure robust and user-friendly behaviour.

 Notes:
     - Flight prices are stored in a dictionary for easy
       maintenance and scalability.
     - User inputs are validated to prevent invalid or
       unexpected values.
===========================================================
"""

# ---------------------------------------------------------
# Functions 
# ---------------------------------------------------------
def hotel_cost(num_nights):
    """Calculate hotel cost based on number of nights."""
    price_per_night = 1200
    return num_nights * price_per_night


def plane_cost(city_flight):
    """Return the flight cost for a valid city."""
    flight_prices = {
        "Cape Town": 2500,
        "Johannesburg": 1800,
        "Durban": 2000,
        "Bloemfontein": 2200
    }
    return flight_prices[city_flight.title()]


def car_rental(rental_days):
    """Calculate car rental cost."""
    daily_rate = 500
    return rental_days * daily_rate


def holiday_cost(num_nights, city_flight, rental_days):
    """Calculate total holiday cost."""
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# ---------------------------------------------------------
# Input Validation Helpers
# ---------------------------------------------------------
def get_valid_city():
    """Prompt user until a valid city is entered."""
    valid_cities = ["Cape Town", "Johannesburg", "Durban", "Bloemfontein"]

    while True:
        city = input("Enter the city you will be flying to (Cape Town, Johannesburg, Durban, Bloemfontein): ").strip().title()
        if city in valid_cities:
            return city
        else:
            print("Invalid city. Please choose one from the list.")


def get_positive_int(prompt):
    """Prompt user until a positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
print("Welcome to the Holiday Cost Calculator!\n")

# ---------------------------
# Get validated user inputs
# ---------------------------
city_flight = get_valid_city()
num_nights = get_positive_int("Enter the number of nights you will stay at the hotel: ")
rental_days = get_positive_int("Enter the number of days you will rent a car: ")

# ---------------------------
# Calculate costs
# ---------------------------
total_hotel = hotel_cost(num_nights)
total_plane = plane_cost(city_flight)
total_car = car_rental(rental_days)
total_holiday = holiday_cost(num_nights, city_flight, rental_days)

# ---------------------------
# Print details
# ---------------------------
print(f"""
{'=' * 55}
{ 'Holiday Cost Summary'.center(55)}
{'-' * 55}
{'Item':<25}{'Details':<20}{'Cost (R)':>10}
{'-' * 55}
{'Destination City':<25}{city_flight.title():<20}{'-':>10}
{'Hotel Stay':<25}{(str(num_nights) + ' nights'):<20}{total_hotel:>10}
{'Car Rental':<25}{(str(rental_days) + ' days'):<20}{total_car:>10}
{'-' * 55}
{'TOTAL HOLIDAY COST':<45}{total_holiday:>10}
""")


# --------------------- END OF CODE -----------------------
