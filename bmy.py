def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return the BMI category based on the calculated BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input(prompt):
    """Safely get numerical input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    """Main function to execute the BMI calculator."""
    print("Welcome to the BMI Calculator!")
    weight = get_user_input("Enter your weight in kilograms: ")
    height = get_user_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\n--- Results ---")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Based on your BMI, you are classified as: {category}")

if __name__ == "__main__":
    main()
