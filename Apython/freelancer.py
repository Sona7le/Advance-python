# Freelancer Marketplace Simulation

freelancers = []
clients = []
projects = []

# Register Freelancer
def register_freelancer():
    name = input("Enter freelancer name: ")
    skill = input("Enter freelancer skill: ")
    
    freelancer = {"name": name, "skill": skill}
    freelancers.append(freelancer)
    
    print("Freelancer registered successfully!\n")

# Register Client
def register_client():
    name = input("Enter client name: ")
    
    client = {"name": name}
    clients.append(client)
    
    print("Client registered successfully!\n")

# Post Project
def post_project():
    title = input("Enter project title: ")
    client = input("Enter client name: ")
    budget = float(input("Enter project budget: "))
    
    project = {
        "title": title,
        "client": client,
        "budget": budget,
        "freelancer": None,
        "paid": False
    }
    
    projects.append(project)
    print("Project posted successfully!\n")

# Assign Project
def assign_project():
    title = input("Enter project title: ")
    freelancer = input("Enter freelancer name: ")
    
    for project in projects:
        if project["title"] == title:
            project["freelancer"] = freelancer
            print("Project assigned successfully!\n")
            return
    
    print("Project not found!\n")

# Payment Processing
def process_payment():
    title = input("Enter project title: ")
    
    for project in projects:
        if project["title"] == title:
            if project["freelancer"] is None:
                print("Project not assigned yet!\n")
            else:
                project["paid"] = True
                print("Payment processed to", project["freelancer"], "\n")
            return
    
    print("Project not found!\n")

# View Projects
def view_projects():
    print("\n--- Projects List ---")
    for p in projects:
        print("Title:", p["title"])
        print("Client:", p["client"])
        print("Freelancer:", p["freelancer"])
        print("Budget:", p["budget"])
        print("Payment Done:", p["paid"])
        print("----------------------")
    print()

# Main Menu
while True:
    print("----- Freelancer Marketplace -----")
    print("1. Register Freelancer")
    print("2. Register Client")
    print("3. Post Project")
    print("4. Assign Project")
    print("5. Process Payment")
    print("6. View Projects")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        register_freelancer()
    elif choice == "2":
        register_client()
    elif choice == "3":
        post_project()
    elif choice == "4":
        assign_project()
    elif choice == "5":
        process_payment()
    elif choice == "6":
        view_projects()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
