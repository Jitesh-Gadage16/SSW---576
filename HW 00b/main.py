from classify_triangle import classify_triangle

def main():
    print("Triangle Classification Program")
    try:
        a = float(input("Enter the first side: "))
        b = float(input("Enter the second side: "))
        c = float(input("Enter the third side: "))
        result = classify_triangle(a, b, c)
        print(f"The triangle is classified as: {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
