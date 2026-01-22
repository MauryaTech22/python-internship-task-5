def add(a, b=0):
    """Returns the sum of two numbers
    """
    return a + b
def subtract(a, b=0):
    """
    Returns the difference of two numbers
    """
    return a - b
def multiply(a, b=1):
    """
    Returns the product of two numbers
    """
    return a * b
def divide(a, b=1):
    """
    Returns the division result of two numbers
    Handles division by zero
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b
def show_menu():
    """
    Displays calculator options
    """
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
def get_numbers():
    """
    Takes two numbers as input from user
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b
def main():
    """
    Main function to run calculator
    """
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "5":
            print("Exiting calculator.")
            break
        if choice in ["1", "2", "3", "4"]:
            a, b = get_numbers()
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
