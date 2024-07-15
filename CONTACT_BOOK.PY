#CONTACT BOOK

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    if len(contacts) == 0:
        print("Contact list is empty.")
    else:
        print("Contact list:")
        for idx, contact in enumerate(contacts):
            print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    keyword = input("Enter keyword to search: ")
    found_contacts = [contact for contact in contacts if keyword.lower() in contact["name"].lower()]
    if len(found_contacts) == 0:
        print("No contacts found.")
    else:
        print("Found contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact():
    view_contact_list()
    idx = int(input("Enter the index of the contact you want to update: ")) - 1
    if idx < 0 or idx >= len(contacts):
        print("Invalid contact index.")
    else:
        name = input("Enter new contact name: ")
        phone = input("Enter new contact phone number: ")
        email = input("Enter new contact email: ")
        
        contacts[idx]["name"] = name
        contacts[idx]["phone"] = phone
        contacts[idx]["email"] = email
        print("Contact updated successfully!")

def delete_contact():
    view_contact_list()
    idx = int(input("Enter the index of the contact you want to delete: ")) - 1
    if idx < 0 or idx >= len(contacts):
        print("Invalid contact index.")
    else:
        del contacts[idx]
        print("Contact deleted successfully!")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()