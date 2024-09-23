# Simple login functionality using Python (simulated)

def login_system():
    print("Welcome to SBL Smart Bots!")
    phone = input("Enter your phone number: ")

    # Check if admin or regular user
    if phone == "0740035058":
        print("Logged in as Admin")
        return "admin"
    else:
        print("Logged in as User")
        return "user"

def main():
    role = login_system()
    
    if role == "admin":
        print("\n--- Admin Homepage ---")
        # Admin dashboard options
        print("1. Upload bot content")
        print("2. View all trading bots")
        # Add more options as needed
    else:
        print("\n--- User Homepage ---")
        # User options
        print("1. View trading bots")
        print("2. Order a bot")

if __name__ == '__main__':
    main()
