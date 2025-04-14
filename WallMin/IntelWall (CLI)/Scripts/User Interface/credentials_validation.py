import getpass

class validation:
    def __init__(self):
        pass

    def email_validation(self, email):
        # Check if the email contains '@' and '.'
        if '@' not in email or '.' not in email:
            return False

        # Check if the email starts with a letter or digit
        if not (email[0].isalpha() or email[0].isdigit()):
            return False

        # Check if the email contains only valid characters
        for char in email:
            if not (char.isalnum() or char in ['@', '.', '_', '-']):
                return False

        # If all checks pass, return True
        return True
    
    def username_validation(self, username):
        # Check if the username is between 4 and 20 characters long
        if len(username) < 4 or len(username) > 20:
            return False

        # Check if the username contains only alphanumeric characters and underscores
        if not all(char.isalnum() or char == '_' for char in username):
            return False

        # If all checks pass, return True
        return True
    
    def password_validation(self, password , confirm_password):
        # Check if the password is between 8 and 12 characters long
        if len(password) < 8 or len(password) > 12:
            return False

        # Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
        if (not any(char.isupper() for char in password) or
                not any(char.islower() for char in password) or
                not any(char.isdigit() for char in password) or
                not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password)):
            return False
        
        if password!= confirm_password:
            print("Passwords do not match. Please try again.")
            return False
        # If all checks pass, return True

        return True
    