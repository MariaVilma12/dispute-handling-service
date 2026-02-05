from dispute import create_dispute, assign_dispute, update_status, list_disputes
from user import list_users
from auth import login, register_user

def menu(role):
    print("\n--- Dispute Management System ---")

    if role == "Admin":
        print("1. Register User")
        print("2. Create Dispute")
        print("3. Assign Dispute")
        print("4. Update Dispute Status")
        print("5. View Disputes")
        print("6. View Users")

    elif role == "Manager":
        print("2. Create Dispute")
        print("3. Assign Dispute")
        print("4. Update Dispute Status")
        print("5. View Disputes")

    elif role == "Viewer":
        print("5. View Disputes")

    print("0. Logout")


# -------- LOGIN --------
print("=== Login ===")
username = input("Username: ")
password = input("Password: ")

user = login(username, password)

if not user:
    print("Invalid credentials.")
    exit()

user_id, name, role = user
print(f"\nWelcome {name} ({role})")

# -------- MAIN LOOP --------
while True:
    menu(role)
    choice = input("Choose an option: ")

    if role == "Admin" and choice == "1":
        name = input("Name: ")
        role_input = input("Role (Admin/Manager/Viewer): ")
        username = input("Username: ")
        password = input("Password: ")
        register_user(name, role_input, username, password)
        print("User registered.")

    elif choice == "2" and role in ["Admin", "Manager"]:
        title = input("Dispute title: ")
        desc = input("Description: ")
        create_dispute(title, desc)
        print("Dispute created.")

    elif choice == "3" and role in ["Admin", "Manager"]:
        dispute_id = int(input("Dispute ID: "))
        user_id = int(input("Assign to User ID: "))
        assign_dispute(dispute_id, user_id)
        print("Dispute assigned.")

    elif choice == "4" and role in ["Admin", "Manager"]:
        dispute_id = int(input("Dispute ID: "))
        status = input("New status: ")
        update_status(dispute_id, status)
        print("Status updated.")

    elif choice == "5":
        disputes = list_disputes()
        for d in disputes:
            print(d)

    elif choice == "6" and role == "Admin":
        users = list_users()
        for u in users:
            print(u)

    elif choice == "0":
        print("Logged out.")
        break

    else:
        print("Access denied or invalid option.")
