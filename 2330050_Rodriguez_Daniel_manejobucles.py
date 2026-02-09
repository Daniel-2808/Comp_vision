
# Problem 1: Sum of integers in a range

# Description:
# Calculates the sum of all integers from 1 to n and the sum of even numbers in the same range using for loops.


n = 10

if isinstance(n, int) and n >= 1:
    total_sum = 0
    even_sum = 0

    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i

    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)
else:
    print("Error: invalid input")


#
# Problem 2: Multiplication table with for
#
# Description:
# Displays the multiplication table of a base number from 1 to m using a for loop.



base = 5
m = 4

if isinstance(base, int) and isinstance(m, int) and m >= 1:
    for i in range(1, m + 1):
        print(f"{base} x {i} = {base * i}")
else:
    print("Error: invalid input")


# Problem 3: Average of numbers with while and sentinel

# Description:
# Reads numbers until a sentinel value is found and calculates the average of valid inputs.


sentinel_value = -1
numbers = [10, 20, 30, -1] 

count = 0
total = 0
index = 0

while True:
    number = numbers[index]
    index += 1

    if number == sentinel_value:
        break

    if number < 0:
        print("Error: invalid input")
        continue

    total += number
    count += 1

if count > 0:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("Error: no data")


# Problem 4: Password attempts with while
# Description:
# Simulates a password check with a limited number of attempts.



CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

password_inputs = ["1234", "admin123", "test"]  

while attempts < MAX_ATTEMPTS:
    user_password = password_inputs[attempts]
    attempts += 1

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
else:
    print("Account locked")



# Problem 5: Simple menu with while
# Description:
# Displays a menu repeatedly until the user selects exit.


counter = 0
options = [1, 3, 2, 0]  
index = 0
option = -1

while option != 0:
    option = options[index]
    index += 1

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")


# Problem 6: Pattern printing with nested loops
# Description:
# Prints a right triangle pattern using nested for loops.



n = 4

if isinstance(n, int) and n >= 1:
    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += "*"
        print(line)
else:
    print("Error: invalid input")
