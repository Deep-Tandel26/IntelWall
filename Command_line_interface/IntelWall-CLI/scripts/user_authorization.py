import getpass
import json
import hashlib
import uuid
import Validations


class User_authorization:
    def __init__(self):
        self.account_type = input("Enter account type (admin/user): ").strip().lower()
        self.name = input("Enter your name: ").strip()
        self.email = input("Enter your email: ").strip()

    def create_unique_id(self):
    # Generate a UUID (Universal Unique Identifier)
        unique_uuid = uuid.uuid4()

    # Combine the name with the UUID to create a unique ID
        self.account_typeunique_id = f"{self.name}_{unique_uuid}"
        return self.unique_id
    

    def User_details(self):
        self.val = False
        self.username = input("Enter username: ").strip()

        while self.val == False:
            self.password = getpass.getpass("Enter password (8-12 characters only): ").strip()
            self.confirm_password = getpass.getpass("Confirm password: ").strip()
            # Validate password using the validation class
            password_validator = Validations.validation().password_validation(self.password)
            if password_validator:
                self.val = True
            else:
                print("Password validation failed. Please try again.")

        self.is_authorized = False #Initially set to False and when the user is authorized it will be set to True


        # Get user details and store them in a dictionary
        user_details = {
            "account_type": self.account_type,
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.confirm_password,  # In a real application, never store passwords in plain text
            "is_authorized": self.is_authorized,
            "id": self.create_unique_id(),
            "filename": self.create_unique_filename()
        }
        return user_details


    def create_unique_filename(self):
    # Create a unique string by combining username and email
        unique_string = f"{self.username}_{self.email}"
    
    # Optionally, use a hash of the string for uniqueness and file safety
        unique_hash = hashlib.md5(unique_string.encode()).hexdigest()
    
    # Generate the JSON file name
        self.filename = f"user_{unique_hash}.json"
    
        return self.filename
