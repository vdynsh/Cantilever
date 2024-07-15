import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Found contact - Name: {name}, Phone: {self.contacts[name]['phone']}, Email: {self.contacts[name]['email']}")
        else:
            print(f"No contact found with the name {name}")

    def edit_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            self.save_contacts()
            print(f"Contact {name} updated successfully.")
        else:
            print(f"No contact found with the name {name}")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"No contact found with the name {name}")

def print_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Quit")

def main():
    contact_book = ContactBook()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to edit: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            contact_book.edit_contact(name, phone, email)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
