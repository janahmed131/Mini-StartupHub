from auth import Auth
from founder import Founder
from freelancer import Freelancer
from investor import Investor

auth = Auth()

while True:

    print("\n========== StartupHub ==========")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        auth.register()

    elif choice == "2":

        user = auth.login()

        if user:

            if user["role"] == "founder":

                founder = Founder(
                    user["name"],
                    user["email"],
                    user["password"]
                )

                founder.founder_menu(user)

            elif user["role"] == "freelancer":

                freelancer = Freelancer(
                    user["name"],
                    user["email"],
                    user["password"],
                    user.get("rating",0)
                )

                freelancer.freelancer_menu()

            elif user["role"] == "investor":

                investor = Investor(
                    user["name"],
                    user["email"],
                    user["password"]
                )

                investor.investor_menu()

            else:
                print("Invalid role.")

    elif choice == "3":
        print("Thank you for using StartupHub!")
        break

    else:
        print("Invalid choice.")