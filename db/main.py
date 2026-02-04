from user import User
from destination import Destination
from booking import Booking

def main():
    print("Welcome to the Travel Management System!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View Destinations")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = User(name=name, email=email, password=password)
            user.register()
        
        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = User.login(email, password)
            if user:
                if user.role == 'admin':
                    print("\nAdmin Menu:")
                    print("1. Add Destination")
                    print("2. Delete Destination")
                    print("3. View All Bookings")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == "1":
                        name = input("Enter destination name: ")
                        description = input("Enter destination description: ")
                        price = float(input("Enter destination price: "))
                        Destination.add_destination(name, description, price)
                    elif admin_choice == "2":
                        destination_id = int(input("Enter destination ID to delete: "))
                        Destination.delete_destination(destination_id)
                    elif admin_choice == "3":
                        pass
                else:
                    print("\nUser Menu:")
                    print("1. View Destinations")
                    print("2. Make a Booking")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        destinations = Destination.view_destinations()
                        for dest in destinations:
                            print(f"{dest[0]}. {dest[1]} - {dest[2]} - ${dest[3]}")
                    elif user_choice == "2":
                        destination_id = int(input("Enter destination ID to book: "))
                        date_of_travel = input("Enter travel date (YYYY-MM-DD): ")
                        Booking.make_booking(user.user_id, destination_id, date_of_travel)
        elif choice == "3":
            destinations = Destination.view_destinations()
            for dest in destinations:
                print(f"{dest[0]}. {dest[1]} - {dest[2]} - ${dest[3]}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
