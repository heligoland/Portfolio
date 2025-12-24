import statistics

def get_int(prompt):
    """
    Safely prompt the user for an integer.
    Continues asking until valid integer input is received.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter an integer value.\n")


# Main program loop (restarts if user enters no valid numbers)
while True:
    
    nums = []  # Stores all valid non-zero integers entered by the user

    # Inner loop: collect numbers until user enters -1
    while (n := get_int("Enter any integer number (-1 to exit): \n")) != -1:

        # Zero is explicitly not allowed
        if n == 0:
            print("Zero is not allowed. Try again.\n")
            continue

        # Valid number → store it
        nums.append(n)

    # After exiting inner loop, check if we have valid numbers
    if nums:
        # Calculate and display the average
        print(f"\nThe average of the numbers you entered is: {statistics.mean(nums)}")
        break  # End program

    # If no valid numbers were entered, restart the outer loop
    print("\nNo valid numbers were entered. Let's try again...\n")
    