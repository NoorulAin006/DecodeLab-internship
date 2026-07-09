print("=" * 50)
print("      PASSWORD SECURITY ANALYSIS TOOL")
print("=" * 50)
print("Check the strength of your password")
print()

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome",
    "abc123"
]

while True:

    password = input("Enter Password: ")

    suggestions = []

    if len(password) < 8:
        suggestions.append("Password must be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if not has_upper:
        suggestions.append("Add at least one uppercase letter.")

    if not has_lower:
        suggestions.append("Add at least one lowercase letter.")

    if not has_digit:
        suggestions.append("Add at least one number.")

    if not has_symbol:
        suggestions.append("Add at least one special character.")

    if password.lower() in common_passwords:
        suggestions.append("This is a common password. Choose a different password.")

    if len(suggestions) == 0:
        print("\n" + "=" * 50)
        print("Password Strength : STRONG")
        print("Password Accepted")
        print("=" * 50)
        break

    else:
        print("\n" + "=" * 50)
        print("Password Strength : WEAK")
        print("Suggestions:")
        print("-" * 50)

        for item in suggestions:
            print("-", item)

        print("\nPlease try again.")
        print("=" * 50)