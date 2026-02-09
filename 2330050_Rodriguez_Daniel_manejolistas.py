
# Problem 1: Shopping list basics (list operations)
# Description:
# Manages a shopping list using a list of products and quantities.
# Allows adding items, counting elements and searching products.


initial_items_text = "apple:2,banana:5,orange:6".strip()
new_item = "grape"
search_item = "banana"

if initial_items_text:
    items_list = []
    for item in initial_items_text.split(","):
        product = item.split(":")[0].strip().lower()
        items_list.append(product)

    if new_item.strip():
        items_list.append(new_item.strip().lower())

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", search_item.strip().lower() in items_list)
else:
    print("Error: invalid input")


# Problem 2: Points and distances with tuples
# Description:
# Uses tuples to represent two 2D points and calculates
# the distance and midpoint.



try:
    x1, y1, x2, y2 = 0.0, 0.0, 3.0, 4.0

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")



# Problem 3: Product catalog with dictionary
# Description:
# Uses a dictionary to store product prices and calculates
# total cost for a given quantity.


product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_name = "apple".strip().lower()
quantity = 3

if product_name and quantity > 0:
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")
else:
    print("Error: invalid input")



# Problem 4: Student grades with dict and list
# Description:
# Manages student grades and calculates averages and pass status.



grades_dict = {
    "alice": [90, 85, 88],
    "bob": [70, 72],
    "carol": [100]
}

student_name = "Alice".strip().lower()

if student_name in grades_dict:
    grades_list = grades_dict[student_name]
    if grades_list:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", is_passed)
    else:
        print("Error: no grades")
else:
    print("Error: student not found")



# Problem 5: Word frequency counter (list + dict)
# Description:
# Counts word frequencies in a sentence.



sentence = "Hello, world! Hello Python.".strip()

if sentence:
    clean_sentence = sentence.lower()
    for symbol in [".", ",", "!", "?", ";", ":"]:
        clean_sentence = clean_sentence.replace(symbol, "")

    words_list = clean_sentence.split()
    freq_dict = {}

    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = max(freq_dict, key=freq_dict.get)

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)
else:
    print("Error: invalid input")



# Problem 6: Simple address book (dictionary CRUD)
# Description:
# Implements a simple address book using dictionary CRUD operations.

contacts = {
    "alice": "1234567890",
    "bob": "5551234"
}

action_text = "ADD".strip().upper()
name = "Carol".strip().lower()
phone = "999888777"

if action_text in ["ADD", "SEARCH", "DELETE"] and name:
    if action_text == "ADD":
        if phone.strip():
            contacts[name] = phone
            print("Contact saved:", name, phone)
        else:
            print("Error: invalid input")

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
else:
    print("Error: invalid input")
