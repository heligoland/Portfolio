# Function to print an arrow pattern
def print_pattern(height, char="*"):
    """Prints a mirrored increasing/decreasing pattern."""
    pattern = list(range(1, height + 1)) + list(range(height - 1, 0, -1))
    for i in pattern:
        print(char * i)


# Example usage:
print_pattern(5, "*")
