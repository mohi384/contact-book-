# === CONTACT BOOK ===

contacts = []

# ---------------- VALIDATION FUNCTIONS ----------------

def validate_name(name):
    name = name.strip()
    if not name:
        return False, "Name cannot be empty!"
    if len(name) < 2:
        return False, "Name must be at least 2 characters long!"
    if not name.replace(" ", "").isalpha():
        return False, "Name can only contain letters and spaces!"
    return True, name

def validate_phone(phone):
    phone = phone.strip().replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    if not phone:
        return False, "Phone number cannot be empty!"
    if not phone.isdigit():
        return False, "Phone number can only contain digits!"
    if len(phone) < 10 or len(phone) > 15:
        return False, "Phone number must be between 10-15 digits!"
    return True, phone

# ---------------- INPUT FUNCTIONS ----------------

def get_valid_name():
    while True:
        name = input("Enter contact name: ")
        is_valid, result = validate_name(name)
        if is_valid:
            return result
        print(f"Error: {result}")

def get_valid_phone():
    while True:
        phone = input("Enter contact's phone number: ")
        is_valid, result = validate_phone(phone)
        if is_valid:
            return result
        print(f"Error: {result}")

def get_valid_choice():
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Error: Please enter 1, 2, 3, 4 or 5 only!")

def get_valid_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes', 'n', 'no']:
            return response
        print("Error: Please enter 'y' for yes or 'n' for no!")

# ---------------- CONTACT FUNCTIONS ----------------

def add_contact():
    print("\n--- ADD CONTACT ---")
    while True:
        name = get_valid_name()
        phone_number = get_valid_phone()

        for contact in contacts:
            if contact['name'].lower() == name.lower():
                print(f"Warning: Contact '{name}' already exists!")
                overwrite = get_valid_yes_no("Do you want to overwrite it? (y/n): ")
                if overwrite in ['y', 'yes']:
                    contact['phone'] = phone_number
                    print(f"{name} updated successfully.")
                break
        else:
            contacts.append({"name": name, "phone": phone_number})
            print(f"{name} added successfully.")

        again = get_valid_yes_no("Do you want to add another contact? (y/n): ")
        if again in ['n', 'no']:
            break

def show_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- CONTACT LIST ---")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    search_name = input("Enter the name to search: ").strip()
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    delete_name = input("Enter the name to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == delete_name.lower():
            contacts.remove(contact)
            print(f"{delete_name} deleted successfully.")
            return
    print("Contact not found.")

# ---------------- MAIN PROGRAM ----------------

def main():
    print("=== CONTACT BOOK ===")
    while True:
        try:
            print("\n--- MENU ---")
            print("1. Add Contact")
            print("2. Show Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = get_valid_choice()

            if choice == "1":
                add_contact()
            elif choice == "2":
                show_contacts()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                delete_contact()
            elif choice == "5":
                print("Thank you for using the Contact Book!")
                break

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

# ---------------- RUN PROGRAM ----------------

if __name__ == "__main__":
    main()
