from application import Application
from user import User
from storage import Storage

class Freelancer(User):

    def __init__(self, name, email, password, rating):
        super().__init__(name, email, password, "freelancer")

        self.rating = rating
        self.skills = ""
        self.experience = ""
        self.badge = "New"
        self.storage = Storage()

    def create_profile(self):
        if self.name == "":
            print("\nName cannot be empty")
            return
        if "@" not in self.email or ".com" not in self.email:
            print("\nInvalid Email")
            return
        if len(self.password) < 6:
            print("\nPassword must be at least 6 characters")
            return
        if self.skills == "":
            print("\nSkills cannot be empty")
            return
        if self.experience == "":
            print("\nExperience cannot be empty")
            return

        users = self.storage.load_data("users.json")
        for user in users:
            if user["email"] == self.email:
                print("\nEmail already exists")
                return

        users = self.storage.load_data("users.json")
        users.append(self.to_dict())
        self.storage.save_data("users.json", users)

    def browse_projects(self):
        projects = self.storage.load_data("projects.json")
        if len(projects) == 0:
            print("\nNo projects found")
            return

        print("\n========== Projects ==========\n")

        for project in projects:
            print("Project Name :", project["project_name"])
            print("ID :", project["project_id"])
            print("Category :", project["category"])
            print("Budget :", project["budget"])
            print("Funding Goal :", project["funding_goal"])
            print("Status :", project["status"])
            print("-" * 30)

    def search_by_category(self):
        projects = self.storage.load_data("projects.json")
        if len(projects) == 0:
            print("\nNo projects found")
            return

        category = input("Enter category : ")
        found = False

        for project in projects:
            if project["category"].lower() == category.lower():
                print("\nProject Name :", project["project_name"])
                print("Category :", project["category"])
                print("Budget :", project["budget"])
                print("Funding Goal :", project["funding_goal"])
                print("Status :", project["status"])
                print("-" * 30)
                found = True

        if not found:
            print("\nNo projects found in this category")

    def search_by_skill(self):
        projects = self.storage.load_data("projects.json")
        if len(projects) == 0:
            print("\nNo projects found")
            return

        search_skill = input("Enter skill : ")
        found = False

        for project in projects:
            for skill in project["required_skills"]:
                if search_skill == skill:
                    print("\nProject Name :", project["project_name"])
                    print("Category :", project["category"])
                    print("Budget :", project["budget"])
                    print("Funding Goal :", project["funding_goal"])
                    print("Status :", project["status"])
                    print("-" * 30)
                    found = True

        if not found:
            print("\nNo projects found in this skill")

    def apply_project(self):
        projects = self.storage.load_data("projects.json")

        if len(projects) == 0:
            print("\nNo projects found")
            return

        print("\n========== Projects ==========\n")

        for project in projects:
            print("Project Name :", project["project_name"])
            print("Project ID :", project["project_id"])
            print("Category :", project["category"])
            print("Budget :", project["budget"])
            print("Funding Goal :", project["funding_goal"])
            print("Status :", project["status"])
            print("-" * 30)

        project_id = int(input("Enter project id : "))

        cover_letter = ""
        for project in projects:
            if project["project_id"] == project_id:
                cover_letter = input("Enter cover letter : ")

        application = Application(self.name, project_id, cover_letter)
        application.submit_application()

    def view_my_application(self):
        applications = self.storage.load_data("applications.json")
        found = False

        for application in applications:
            if application["freelancer_name"] == self.name:
                print("\nFreelancer name :", application["freelancer_name"])
                print("Project ID :", application["project_id"])
                print("Cover Letter :", application["cover_letter"])
                print("Status :", application["status"])
                print("-" * 30)
                found = True

        if not found:
            print("\nNo applications found")

    def view_completed_projects(self):
        projects = self.storage.load_data("projects.json")
        applications = self.storage.load_data("applications.json")
        found = False

        for application in applications:
            if application["freelancer_name"] == self.name:
                if application["status"] == "Accepted":
                    for project in projects:
                        if project["project_id"] == application["project_id"]:
                            if project["status"] == "Completed":
                                print("\nProject name :", project["project_name"])
                                print("Project category :", project["category"])
                                print("Project budget :", project["budget"])
                                print("-" * 30)
                                found = True

        if not found:
            print("\nNo completed projects found")

    def view_earnings(self):
        projects = self.storage.load_data("projects.json")
        applications = self.storage.load_data("applications.json")
        total = 0

        for application in applications:
            if application["freelancer_name"] == self.name:
                if application["status"] == "Accepted":
                    for project in projects:
                        if project["project_id"] == application["project_id"]:
                            if project["status"] == "Completed":
                                total += project["budget"]

        if total == 0:
            print("\nNo Earnings found")
        else:
            print("\nTotal Earnings :", total)

    def view_rating(self):
        print("\nYour rating :", self.rating)

    def view_badge(self):
        self.update_badge()
        print("\nYour badge :", self.badge)

    def update_badge(self):
        applications = self.storage.load_data("applications.json")
        projects = self.storage.load_data("projects.json")
        completed_projects = 0

        for application in applications:
            if application["freelancer_name"] == self.name:
                if application["status"] == "Accepted":
                    for project in projects:
                        if project["project_id"] == application["project_id"]:
                            if project["status"] == "Completed":
                                completed_projects += 1

        if completed_projects >= 50:
            self.badge = "Elite"
        elif completed_projects >= 15:
            self.badge = "Expert"
        elif completed_projects >= 5:
            self.badge = "Professional"
        elif completed_projects >= 1:
            self.badge = "Rookie"
        else:
            self.badge = "New"

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": "freelancer",
            "skills": self.skills,
            "experience": self.experience,
            "rating": self.rating,
            "badge": self.badge
        }

    def freelancer_menu(self):
        while True:

            print("\n===== Freelancer Menu =====\n")
            print("1- Browse projects")
            print("2- Search by category")
            print("3- Search by skill")
            print("4- Apply for project")
            print("5- View my applications")
            print("6- View completed projects")
            print("7- View earnings")
            print("8- View rating")
            print("9- View badge")
            print("10- Logout")
            print("-" * 30)

            choice = int(input("Enter your choice : "))

            if choice == 1:
                self.browse_projects()
            elif choice == 2:
                self.search_by_category()
            elif choice == 3:
                self.search_by_skill()
            elif choice == 4:
                self.apply_project()
            elif choice == 5:
                self.view_my_application()
            elif choice == 6:
                self.view_completed_projects()
            elif choice == 7:
                self.view_earnings()
            elif choice == 8:
                self.view_rating()
            elif choice == 9:
                self.view_badge()
            elif choice == 10:
                print("\nThank you for using Freelancer")
                break
            else:
                print("\nInvalid choice")