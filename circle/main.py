import mainthing

def print_circle(radius):
    # Determine the square bounds of the circle
    for i in range((2 * radius) + 1):
        for j in range((2 * radius) + 1):
            # Translate loop counter to Cartesian coordinates (x, y)
            x = i - radius
            y = j - radius
            # Use the circle equation (x^2 + y^2 = r^2) to check if point is inside the circle
            if (x**2 + y**2 <= radius**2):
                print('*', end='')
            else:
                print(' ', end='')
        print()  # Newline for the next row
mainthing.check()

print_circle(10)
