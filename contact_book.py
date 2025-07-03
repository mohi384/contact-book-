contacts = []

def validate_name(name):
    """Validate contact name input"""
    name = name.strip()
    if not name:
        return False, "Name cannot be empty!"
    if len(name) < 2:
        return False, "Name must be at least 2 characters long!"
    if not name.replace(" ", "").isalpha():
        return False, "Name can only contain letters and spaces!"
    return True, name

def validate_phone(phone):
    """Validate phone number input"""
    phone = phone.strip().replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    if not phone:
        return False, "Phone number cannot be empty!"
    if not phone.isdigit():
        return False, "Phone number can only contain digits!"
    if len(phone) < 10 or len(phone) > 15:
        return False, "Phone number must be between 10-15 digits!"
    return True, phone

def get_valid_name():
    """Get a valid name from user input"""
    while True:
        name = input("Enter contact name: ")
        is_valid, result = validate_name(name)
        if is_valid:
            return result
        else:
            print(f"Error: {result}")

def get_valid_phone():
    """Get a valid phone number from user input"""
    while True:
        phone = input("Enter contact's phone number: ")
        is_valid, result = validate_phone(phone)
        if is_valid:
            return result
        else:
            print(f"Error: {result}")

def get_valid_choice():
    """Get a valid menu choice from user input"""
    while True:
        choice = input("Enter your choice(1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Error: Please enter 1, 2, or 3 only!")

def get_valid_yes_no():
    """Get a valid yes/no response from user input"""
    while True:
        response = input("Do you want to add another contact?(y/n): ").strip().lower()
        if response in ['y', 'yes', 'n', 'no']:
            return response
        else:
            print("Error: Please enter 'y' for yes or 'n' for no!")

def show_contact():
  if not contacts:
    print("no contacts found.")
  else:
    print("\n---contact list---")
    for contact in contacts:
      print(f"Name: {contact['name']}, Phone: {contact['phone']}")
print("=== CONTACT BOOK ===")

while True:
    try:
        print("\n--- MENU ---")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Exit")
        
        choice = get_valid_choice()
        
        if choice == "1":
            print("\n--- ADD CONTACT ---")
            while True:
                # Get validated inputs
                name = get_valid_name()
                phone_number = get_valid_phone()
                
                # Check if contact already exists
                contact_exists = False
                for contact in contacts:
                    if contact['name'].lower() == name.lower():
                        print(f"Warning: Contact '{name}' already exists!")
                        overwrite = input("Do you want to overwrite it? (y/n): ").strip().lower()
                        if overwrite in ['y', 'yes']:
                            contact['phone'] = phone_number
                            print(f"{name} updated successfully.")
                        contact_exists = True
                        break
                
                if not contact_exists:
                    contacts.append({"name": name, "phone": phone_number})
                    print(f"{name} added successfully.")
                
                # Ask if user wants to add another contact
                add_another = get_valid_yes_no()
                if add_another in ['n', 'no']:
                    break
                    
        elif choice == "2":
            show_contact()
            
        elif choice == "3":
            print("Thank you for using the Contact Book!")
            break
            
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.")



