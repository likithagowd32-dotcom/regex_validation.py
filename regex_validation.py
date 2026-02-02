import re

# Email validation function
def validate_email(email):
    if not email:
        return "Email cannot be empty"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return "Valid Email Address"
    else:
        return "Invalid Email Address"


# Indian mobile number validation function
def validate_mobile(mobile):
    if not mobile:
        return "Mobile number cannot be empty"
    pattern = r'^[6-9]\d{9}$'
    if re.fullmatch(pattern, mobile):
        return "Valid Indian Mobile Number"
    else:
        return "Invalid Mobile Number"


# Password validation function
def validate_password(password):
    if not password:
        return "Password cannot be empty"
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    if re.fullmatch(pattern, password):
        return "Strong Password"
    else:
        return ("Invalid Password\n"
                "Password must contain:\n"
                "- Minimum 8 characters\n"
                "- At least one uppercase letter\n"
                "- One lowercase letter\n"
                "- One digit\n"
                "- One special character (@$!%*?&)")


# Main program
if __name__ == "__main__":
    print("=== REGEX VALIDATION PROJECT ===")

    email_input = input("Enter Email: ")
    print(validate_email(email_input))

    mobile_input = input("Enter Indian Mobile Number: ")
    print(validate_mobile(mobile_input))

    password_input = input("Enter Password: ")
    print(validate_password(password_input))
