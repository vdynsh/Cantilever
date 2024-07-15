import json
import tkinter as tk
from tkinter import messagebox

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
            return "No contacts found."
        else:
            contact_list = []
            for name, details in self.contacts.items():
                contact_list.append(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
            return "\n".join(contact_list)

class ContactBookApp:
    def __init__(self, root, contact_book):
        self.contact_book = contact_book
        self.root = root
        self.root.title("Contact Book")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            self.contact_book.add_contact(name, phone, email)
            messagebox.showinfo("Success", f"Contact {name} added successfully.")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def view_contacts(self):
        contacts = self.contact_book.view_contacts()
        messagebox.showinfo("Contacts", contacts)

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook()
    app = ContactBookApp(root, contact_book)
    root.mainloop()
