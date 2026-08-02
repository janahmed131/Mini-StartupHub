from storage import Storage
from user import User
from application import Application


class Founder(User):

    def __init__(self, name, email, password):
        super().__init__(name, email, password, "founder")
        self.storage = Storage()

    def create_project(self, user):

        projects = self.storage.load_data("projects.json")

        project_id = len(projects) + 1
        project_name = input("Enter project name: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        required_skills = input(
            "Enter required skills (comma separated): "
        ).split(",")

        budget = float(input("Enter budget: "))
        funding_goal = float(input("Enter funding goal: "))

        new_project = {
            "project_id": project_id,
            "project_name": project_name,
            "category": category,
            "description": description,
            "required_skills": required_skills,
            "budget": budget,
            "funding_goal": funding_goal,
            "status": "Open",
            "founder_email": user["email"]
        }

        projects.append(new_project)

        self.storage.save_data("projects.json", projects)

        print("Project created successfully.")

    def view_projects(self, user):

        projects = self.storage.load_data("projects.json")

        for project in projects:

            if project["founder_email"] == user["email"]:

                print("Project ID:", project["project_id"])
                print("Project Name:", project["project_name"])
                print("Category:", project["category"])
                print("Description:", project["description"])
                print("Required Skills:", project["required_skills"])
                print("Budget:", project["budget"])
                print("Funding Goal:", project["funding_goal"])
                print("Status:", project["status"])
                print("-" * 30)

    def edit_project(self, user):

        projects = self.storage.load_data("projects.json")

        project_name = input("Enter project name to edit: ")

        for project in projects:

            if (
                project["project_name"] == project_name
                and project["founder_email"] == user["email"]
            ):

                project["project_name"] = input("Enter new project name: ")
                project["category"] = input("Enter new category: ")
                project["description"] = input("Enter new description: ")
                project["required_skills"] = input(
                    "Enter required skills: "
                ).split(",")

                project["budget"] = float(
                    input("Enter new budget: ")
                )

                project["funding_goal"] = float(
                    input("Enter new funding goal: ")
                )

                self.storage.save_data("projects.json", projects)

                print("Project updated successfully.")
                return

        print("Project not found.")

    def delete_project(self, user):

        projects = self.storage.load_data("projects.json")

        project_name = input("Enter project name to delete: ")

        for project in projects:

            if (
                project["project_name"] == project_name
                and project["founder_email"] == user["email"]
            ):

                projects.remove(project)

                self.storage.save_data("projects.json", projects)

                print("Project deleted successfully.")
                return

        print("Project not found.")

    def manage_application(self):

        applications = self.storage.load_data("applications.json")

        if len(applications) == 0:
            print("No applications found.")
            return

        for application in applications:

            print("\nFreelancer Name:", application["freelancer_name"])
            print("Project ID:", application["project_id"])
            print("Cover Letter:", application["cover_letter"])
            print("Status:", application["status"])
            print("-" * 30)

        project_id = int(input("Enter project ID: "))
        freelancer_name = input("Enter freelancer name: ")

        for application in applications:

            if (
                application["project_id"] == project_id
                and application["freelancer_name"] == freelancer_name
            ):

                choice = input("Accept or Reject? ").lower()

                if choice == "accept":
                    application["status"] = "Accepted"

                elif choice == "reject":
                    application["status"] = "Rejected"

                else:
                    print("Invalid choice.")
                    return

                self.storage.save_data(
                    "applications.json",
                    applications
                )

                print("Application updated successfully.")
                return

        print("Application not found.")

    def rate_freelancer(self):

         users = self.storage.load_data("users.json")

         freelancer_name = input("Enter freelancer name: ")

         for user in users:

          if user["name"] == freelancer_name and user["role"] == "freelancer":

            rating = int(input("Enter rating (1-5): "))

            while rating < 1 or rating > 5:
                print("Rating must be between 1 and 5.")
                rating = int(input("Enter rating (1-5): "))

                user["rating"] = rating

                self.storage.save_data("users.json", users)

                print("Rating added successfully.")
                return

                print("Freelancer not found.")


    def founder_menu(self, user):

        while True:

            print("\n=== Founder Menu ===")

            print("""
1. Create Project
2. View My Projects
3. Edit Project
4. Delete Project
5. Manage Applications
6. Rate freelancer
7. Logout
""")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.create_project(user)

            elif choice == "2":

                self.view_projects(user)

            elif choice == "3":

                self.edit_project(user)

            elif choice == "4":

                self.delete_project(user)

            elif choice == "5":

                self.manage_application()

            elif choice=="6":
                self.rate_freelancer()

            elif choice == "7":

                print("Logged out successfully.")
                break

            else:

                print("Invalid choice.")