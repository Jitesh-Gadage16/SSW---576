"""
Module: classify_triangle
This module contains a function to classify triangles based on their side lengths.
"""

def classify_triangle(a, b, c):
    """
    Determines the type of triangle based on given side lengths.

    Parameters:
    a (float): Length of first side
    b (float): Length of second side
    c (float): Length of third side

    Returns:
    str: Type of triangle (Equilateral, Isosceles, Scalene, Right Triangle, or Not a Triangle)
    """

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if round(a**2 + b**2, 5) == round(c**2, 5) or \
       round(a**2 + c**2, 5) == round(b**2, 5) or \
       round(b**2 + c**2, 5) == round(a**2, 5):
        return f"{triangle_type} and Right Triangle"

    return triangle_type

# Ensure the file ends with a newline (fix for C0304)
