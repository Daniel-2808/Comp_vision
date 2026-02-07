
# Problem 1: Rectangle area and perimeter
# Description:
# This problem calculates the area and perimeter of a rectangle using two separate functions.


def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


width = 5
height = 3

if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")



# Problem 2: Grade classifier
# Description:
# Classifies a numeric grade into a letter category.


def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score = 85

if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")


# Problem 3: List statistics (min, max, average)
# Description:
# Receives a list of numbers and returns min, max and average.


def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


numbers_text = "10,20,30"
numbers_text = numbers_text.strip()

if numbers_text:
    try:
        numbers_list = [float(n.strip()) for n in numbers_text.split(",")]
        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            summary = summarize_numbers(numbers_list)
            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])
    except ValueError:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# Problem 4: Apply discount list
# Description:
# Applies a discount to a list of prices without modifying the original list.



def apply_discount(prices_list, discount_rate):
    discounted_prices = []
    for price in prices_list:
        discounted_prices.append(price * (1 - discount_rate))
    return discounted_prices


prices_text = "100,200,300"
discount_rate = 0.10

prices_text = prices_text.strip()

if prices_text and 0 <= discount_rate <= 1:
    try:
        prices_list = [float(p.strip()) for p in prices_text.split(",")]
        if all(price > 0 for price in prices_list):
            discounted = apply_discount(prices_list, discount_rate)
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted)
        else:
            print("Error: invalid input")
    except ValueError:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# Problem 5: Greeting function with default parameters
# Description:
# Generates a greeting using a name and an optional title.



def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name

    return f"Hello, {full_name}!"


name = "Alice"
title = "Dr."

if name.strip():
    print("Greeting:", greet(name=name, title=title))
else:
    print("Error: invalid input")



# Problem 6: Factorial function
# Description:
# Calculates the factorial of a non-negative integer.
# Iterative version chosen for clarity and simplicity.


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 5

if isinstance(n, int) and 0 <= n <= 20:
    print("n:", n)
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")
