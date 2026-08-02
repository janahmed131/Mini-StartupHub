from storage import Storage
import random

class Auth:

    def __init__(self):
        self.storage = Storage()

    def register(self):

        users = self.storage.load_data("users.json")

        name = input("Enter your name: ")
        email = input("Email: ")

        while "@" not in email or "." not in email:
            print("Invalid Email")
            email = input("Email: ")

        for user in users:
            if email == user["email"]:
                print("Email already exists.")
                return

        password = input("Password: ")

        while len(password) < 6:
            print("Password must be at least 6 characters")
            password = input("Password: ")

        while True:

            role = input("Enter your role (founder/freelancer/investor): ").lower()

            if role in ["founder", "freelancer", "investor"]:
                break

            print("Invalid role.")

        new_user = {
            "name": name,
            "id": random.randint(1000, 9999),
            "email": email,
            "password": password,
            "role": role
        }

        users.append(new_user)

        self.storage.save_data("users.json", users)

        print("Registration successful.")

    def login(self):

        users = self.storage.load_data("users.json")

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in users:

            if email == user["email"] and password == user["password"]:

                print("Login successful.")
                return user

        print("Invalid email or password.")
        return None