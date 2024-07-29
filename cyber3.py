import re

def assess_password_strength(password):
    feedback = []
    strength = 0

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    else:
        strength += 1
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength += 1

    # Determine overall strength
    if strength == 5:
        feedback.append("Password is very strong.")
    elif strength == 4:
        feedback.append("Password is strong.")
    elif strength == 3:
        feedback.append("Password is average.")
    elif strength == 2:
        feedback.append("Password is weak.")
    else:
        feedback.append("Password is very weak.")
    
    return feedback

# Example usage:
password = input("Enter your password: ")
feedback = assess_password_strength(password)
for line in feedback:
    print(line)
