from user import User
from storage import Storage
from investment import Investment
from datetime import datetime
from dashboard import Dashboard

class Investor(User):

    def __init__(self, name, email, password):
        super().__init__(name, email, password, "investor")
        self.storage = Storage()

    def browse_projects(self):
        projects = self.storage.load_data("projects.json")

        if len(projects) == 0:
            print("\nNo Projects Found.\n")
            return

        print("\n========== Projects ==========\n")

        for project in projects:
            print("Project Name :", project["project_name"])
            print("Category :", project["category"])
            print("Budget :", project["budget"])
            print("Funding Goal :", project["funding_goal"])
            print("Status :", project["status"])
            print("-" * 30)

    def invest(self):
        projects = self.storage.load_data("projects.json")

        if len(projects) == 0:
            print("No Projects Available.")
            return

        project_name = input("Enter Project Name: ")
        found = False

        for project in projects:
            if project["project_name"].lower() == project_name.lower():
                found = True
                amount = float(input("Enter amount: "))

                while amount <= 0:
                    print("Invalid amount")
                    amount = float(input("Enter amount: "))

                investment = Investment(
                    self.name,
                    project_name,
                    amount,
                    datetime.now().strftime("%Y-%m-%d")
                )

                investments = self.storage.load_data("investments.json")
                investments.append(investment.to_dict())

                self.storage.save_data("investments.json", investments)

                print("\nInvestment Successful.\n")
                break

        if not found:
            print("Project Not Found.")

    def my_investments(self):
        investments = self.storage.load_data("investments.json")

        print("\n========== My Investments ==========\n")
        found = False

        for item in investments:
            if item["investor"] == self.name:
                found = True
                print("Project :", item["project"])
                print("Amount :", item["amount"])
                print("Date :", item["date"])
                print("-" * 25)

        if not found:
            print("No Investments Yet.")

    def funded_projects(self):


        investments = self.storage.load_data("investments.json")
        # print("Inside funded_projects") 
        # print(investments)      # للتجربة
        if len(investments) == 0:
         print("\nNo Funded Projects.\n")
         return

        print("\n========== Funded Projects ==========\n")

        funded = []

        for investment in investments:
         if investment["project"] not in funded:
            funded.append(investment["project"])

        for project in funded:
          print(project)

    def investor_menu(self):
        
        while True:
            print ("\n=== investor menu====\n")
            print("""
1. Browse Projects
2. Invest
3. My Investments
4. Funded Projects
5. Dashboard
6. Logout
""")

            choice = input("Choose: ")

            if choice == "1":
                self.browse_projects()

            elif choice == "2":
                self.invest()

            elif choice == "3":
                self.my_investments()

            elif choice == "4":
    
        
                self.funded_projects()

            elif choice == "5":
                dashboard = Dashboard()
                dashboard.show_dashboard()

            elif choice == "6":
                break

            else:
                print("Invalid Choice")