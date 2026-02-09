
# Problem 1: Temperature converter and range flag

# Description:
# Converts temperature from Celsius to Fahrenheit and Kelvin and determines if it is a high temperature.


temp_c = 35.0

try:
    temp_c = float(temp_c)
    if temp_c >= -273.15:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")



# Problem 2: Work hours and overtime payment
# Description:
# Calculates weekly pay including overtime and determines if overtime was worked.



hours_worked = 45
hourly_rate = 100.0

if isinstance(hours_worked, int) and hours_worked >= 0 and hourly_rate > 0:
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40

    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", has_overtime)
else:
    print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description:
# Determines discount eligibility based on student, senior status or purchase amount.


purchase_total = 1200.0
is_student_text = "NO"
is_senior_text = "NO"

is_student_text = is_student_text.strip().upper()
is_senior_text = is_senior_text.strip().upper()

if purchase_total >= 0 and is_student_text in ["YES", "NO"] and is_senior_text in ["YES", "NO"]:
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    print("Discount eligible:", discount_eligible)
    print("Final total:", final_total)
else:
    print("Error: invalid input")



# Problem 4: Basic statistics of three integers
# Description:
# Calculates sum, average, min, max and checks if all numbers are even.


try:
    n1, n2, n3 = 2, 4, 6

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except ValueError:
    print("Error: invalid input")



# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Determines loan eligibility based on income, debt ratio and credit score.


monthly_income = 10000.0
monthly_debt = 3000.0
credit_score = 700

if monthly_income > 0 and monthly_debt >= 0 and credit_score >= 0:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

    print("Debt ratio:", debt_ratio)
    print("Eligible:", eligible)
else:
    print("Error: invalid input")



# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# Calculates BMI and determines weight category using booleans.

weight_kg = 70.0
height_m = 1.75

if weight_kg > 0 and height_m > 0:
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)

    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0

    print("BMI:", bmi_rounded)
    print("Underweight:", is_underweight)
    print("Normal:", is_normal)
    print("Overweight:", is_overweight)
else:
    print("Error: invalid input")
