from storage import Storage

class Application:
    def __init__(self,freelancer_name,project_id,cover_letter):
        self.freelancer_name = freelancer_name
        self.project_id = project_id
        self.cover_letter = cover_letter
        self.status = "Pending"
        self.storage = Storage()


    def submit_application(self):
        applications = self.storage.load_data("applications.json")
        applications.append(self.to_dict())
        self.storage.save_data("applications.json",applications)


    def update_status(self,new_status):
        if new_status in ["Accepted", "Rejected"]:
            self.status = new_status
        else:
            print("Invalid status")




    def to_dict(self):
        return {
            "freelancer_name": self.freelancer_name,
            "project_id": self.project_id,
            "cover_letter": self.cover_letter,
            "status": self.status
        }

