def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    elif not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    elif not any(char in "!@#$%^&*()-+" for char in password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Password meets all requirements."
password  = input("Enter Password: ")
print(check_password_strength(password))

