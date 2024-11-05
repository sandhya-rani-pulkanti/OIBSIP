# Helper function to get valid input for height and weight
def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("Oops! That's not a valid number. Please enter a numeric value.")

# Get height and weight inputs with simple validation
height = get_valid_input("Enter height in meters (1.0 to 2.5): ", 1.0, 2.5)
weight = get_valid_input("Enter weight in kilograms (10 to 250): ", 10, 250)

# Function to calculate BMI and return category and value
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 16:
        return "severely underweight", bmi
    elif 16 <= bmi < 17:
        return "moderately underweight", bmi
    elif 17 <= bmi < 18.5:
        return "mildly underweight", bmi
    elif 18.5 <= bmi < 25:
        return "normal weight", bmi
    elif 25 <= bmi < 30:
        return "overweight", bmi
    elif 30 <= bmi < 35:
        return "obese class I (moderate)", bmi
    elif 35 <= bmi < 40:
        return "obese class II (severe)", bmi
    else:
        return "obese class III (very severe)", bmi

# Run the function and display the result
status, bmi_value = calculate_bmi(height, weight)
print("Your BMI is: {:.2f} and you are: {}".format(bmi_value, status))
