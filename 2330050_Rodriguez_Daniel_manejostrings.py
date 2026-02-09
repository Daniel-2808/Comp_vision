# ==================================================
# Programming Assignment: Strings in Python
# String manipulation, validation and formatting
# ==================================================


# ==================================================
# Problem 1: Full name formatter (name + initials)
# ==================================================
# Description:
# Formats a full name into Title Case and generates initials.

# Inputs:
# - full_name (string)

# Outputs:
# - "Formatted name:"
# - "Initials:"

# Validation:
# - full_name not empty
# - At least two words

# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Edge case: "  maria lopez  "
# 3) Error: "juan"


full_name = "juan carlos tovar".strip()

if full_name and len(full_name.split()) >= 2:
    normalized_name = " ".join(full_name.split()).title()
    name_parts = normalized_name.split()

    initials = ""
    for part in name_parts:
        initials += part[0].upper() + "."

    print("Formatted name:", normalized_name)
    print("Initials:", initials)
else:
    print("Error: invalid input")


# ==================================================
# Problem 2: Simple email validator (structure + domain)
# ==================================================
# Description:
# Validates a basic email structure and extracts the domain.

# Inputs:
# - email_text (string)

# Outputs:
# - "Valid email:"
# - "Domain:" (if valid)

# Validation:
# - Exactly one '@'
# - No spaces

# Test cases:
# 1) Normal: "user@mail.com"
# 2) Edge case: "test@domain.co"
# 3) Error: "user@@mail.com"


email_text = "user@mail.com".strip()

if email_text and email_text.count("@") == 1 and " " not in email_text:
    at_index = email_text.find("@")
    domain = email_text[at_index + 1:]

    if "." in domain:
        print("Valid email:", True)
        print("Domain:", domain)
    else:
        print("Valid email:", False)
else:
    print("Valid email:", False)


# ==================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# ==================================================
# Description:
# Checks if a phrase is a palindrome ignoring spaces and case.

# Inputs:
# - phrase (string)

# Outputs:
# - "Is palindrome:"

# Validation:
# - Phrase not empty
# - Minimum length after cleaning

# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Edge case: "oso"
# 3) Error: ""


phrase = "Anita lava la tina".strip()

if phrase:
    cleaned_phrase = phrase.lower().replace(" ", "")
    if len(cleaned_phrase) >= 3:
        is_palindrome = cleaned_phrase == cleaned_phrase[::-1]
        print("Is palindrome:", is_palindrome)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


# ==================================================
# Problem 4: Sentence word statistics
# ==================================================
# Description:
# Analyzes words in a sentence and shows statistics.

# Inputs:
# - sentence (string)

# Outputs:
# - Word count, first, last, shortest and longest word

# Validation:
# - Sentence not empty

# Test cases:
# 1) Normal: "Python is very powerful"
# 2) Edge case: "Hello"
# 3) Error: ""


sentence = "Python is very powerful".strip()

if sentence:
    words = sentence.split()
    word_count = len(words)

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", word_count)
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)
else:
    print("Error: invalid input")


# ==================================================
# Problem 5: Password strength classifier
# ==================================================
# Description:
# Classifies a password as weak, medium or strong.

# Inputs:
# - password_input (string)

# Outputs:
# - "Password strength:"

# Validation:
# - Password not empty

# Test cases:
# 1) Normal: "Abc123!@"
# 2) Edge case: "password"
# 3) Error: ""


password_input = "Abc123!@".strip()

if password_input:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if len(password_input) >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif len(password_input) >= 8 and (has_upper or has_lower) and has_digit:
        strength = "medium"
    else:
        strength = "weak"

    print("Password strength:", strength)
else:
    print("Error: invalid input")


# ==================================================
# Problem 6: Product label formatter (fixed-width text)
# ==================================================
# Description:
# Formats a product label with exactly 30 characters.

# Inputs:
# - product_name (string)
# - price_value (number)

# Outputs:
# - "Label:"

# Validation:
# - product_name not empty
# - price_value positive

# Test cases:
# 1) Normal: "Notebook", 25.5
# 2) Edge case: long product name
# 3) Error: price_value < 0


product_name = "Notebook".strip()
price_value = 25.5

if product_name and price_value > 0:
    base_label = f"Product: {product_name} | Price: ${price_value}"
    if len(base_label) < 30:
        label = base_label + " " * (30 - len(base_label))
    else:
        label = base_label[:30]

    print('Label:', f'"{label}"')
else:
    print("Error: invalid input")
