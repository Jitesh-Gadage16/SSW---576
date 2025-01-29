def classify_triangle(a, b , c):

    if a + b <= c or a + c <= b or b+c <= a:
        return "Not a Triangle"
    
    if a == b == c:
        return "Equilateral"
    
    if a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"


    if round(a**2 + b**2, 5) == round(c**2,5) or \
       round(a**2 + c**2, 5) == round(b**2,5) or \
       round(b**2 + c**2, 5) == round(a**2,5):
        return f"{triangle_type} and Right Triangle"



    return triangle_type