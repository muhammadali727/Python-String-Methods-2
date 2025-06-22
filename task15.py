password = input("Parolni kiriting: ")

has_digit = any(char.isdigit() for char in password)

print(has_digit)