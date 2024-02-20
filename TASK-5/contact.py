class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone_number']}")

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone_number']:
                results.append((name, details))
        return results

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        contact = self.contacts[name]
        if phone_number:
            contact['phone_number'] = phone_number
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        print("Contact updated successfully.")

    def delete_contact(self, name):
        if name not in self.contacts:
            print("Contact not found.")
            return
        del self.contacts[name]
        print("Contact deleted successfully.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("Search Results:")
                for name, details in results:
                    print(f"Name: {name}, Phone: {details['phone_number']}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (leave empty to keep unchanged): ")
            email = input("Enter new email (leave empty to keep unchanged): ")
            address = input("Enter new address (leave empty to keep unchanged): ")
            contact_book.update_contact(name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
