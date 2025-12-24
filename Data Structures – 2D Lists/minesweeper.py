"""
────────────────────────────────────────────────────────────
Minesweeper Game
────────────────────────────────────────────────────────────
"""

def count_adjacent_mines(grid, row, col):
    """
    Count the number of '#' cells adjacent to position (row, col).
    Adjacent means 8 directions: N, NE, E, SE, S, SW, W, NW.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Offsets for the 8 neighboring cells (and the center which we will skip)
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # Skip the current cell itself
            if dr == 0 and dc == 0:
                continue

            new_row = row + dr
            new_col = col + dc

            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == "#":
                    count += 1

    return count


def minesweeper(grid):
    """
    Takes a grid (list of lists) of '#' and '-'.
    Returns a new grid where:
      - '#' stays '#'
      - '-' is replaced with the number of adjacent mines.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Create a new grid for the result
    result = []

    for r in range(rows):
        # Start a new row for the result
        result_row = []
        for c in range(cols):
            if grid[r][c] == "#":
                # Keep mines as they are
                result_row.append("#")
            else:
                # Count neighboring mines and append the number
                mine_count = count_adjacent_mines(grid, r, c)
                result_row.append(mine_count)
        # Add the completed row to the result grid
        result.append(result_row)

    return result


# Example usage
if __name__ == "__main__":
    input_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    output_grid = minesweeper(input_grid)

    # Print the result in a readable way
    for row in output_grid:
        print(row)

# --------------------- END OF CODE ------------------------
