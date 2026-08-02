import pandas as pd
import matplotlib.pyplot as plt
from storage import Storage
from tabulate import tabulate
class Dashboard:

    def __init__(self):
        self.storage = Storage()

    def show_dashboard(self):
        users = self.storage.load_data("users.json")
        projects = self.storage.load_data("projects.json")
        investments = self.storage.load_data("investments.json")

        print("\n===== DASHBOARD =====\n")
        print("Total Users :", len(users))
        print("Total Projects :", len(projects))

        if len(projects) > 0:
            
            print("\n========== Projects Table ==========\n")
            print(tabulate(projects, headers="keys", tablefmt="psql"))

            df = pd.DataFrame(projects)
            if "status" in df.columns:
                status_count = df["status"].value_counts()
            else:
                status_count = {}
            open_projects = status_count.get("Open", 0)
            completed_projects = status_count.get("Completed", 0)

            print("Open Projects :", open_projects)
            print("Completed Projects :", completed_projects)
        else:
            open_projects = 0
            completed_projects = 0
            print("Open Projects : 0")
            print("Completed Projects : 0")

        if len(investments) > 0:
            print("\n========== Investments Table ==========\n")
            print(tabulate(investments, headers="keys", tablefmt="psql"))

            invest_df = pd.DataFrame(investments)
            funded = invest_df["project"].nunique()
            print("Funded Projects :", funded)

            investor = invest_df.groupby("investor")["amount"].sum()
            print("Top Investor :", investor.idxmax())
        else:
            print("Funded Projects : 0")
            print("Top Investor : None")

        self.project_chart(open_projects, completed_projects)

    def project_chart(self, open_projects, completed_projects):
        status = ["Open", "Completed"]
        count = [open_projects, completed_projects]

        plt.figure(figsize=(6,4))
        plt.bar(status, count)
        plt.title("Projects Status")
        plt.xlabel("Status")
        plt.ylabel("Number of Projects")
        plt.show()