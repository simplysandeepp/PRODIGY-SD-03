def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n=== Contact List ===")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("Leave blank to keep current value.")

            new_name = input(f"New name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New email ({contact['email']}): ") or contact['email']

            contact.update({"name": new_name, "phone": new_phone, "email": new_email})
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Contact '{deleted['name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")
