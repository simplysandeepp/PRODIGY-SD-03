from contact_manager import add_contact, view_contacts, edit_contact, delete_contact
import storage

def main():
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        contacts = storage.load_contacts()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            storage.save_contacts(contacts)
            print("Exiting... Contacts saved.")
            break
        else:
            print("Invalid choice. Please try again.")

        storage.save_contacts(contacts)

if __name__ == "__main__":
    main()