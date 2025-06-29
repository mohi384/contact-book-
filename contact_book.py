contacts = []
def show_contact():
  if not contacts:
    print("no contacts found.")
  else:
    print("\n---contact list---")
    for contact in contacts:
      print(f"Name: {contact['name']},phone:{contact['phone']}")
while True:
    print("1. Add Contact")
    print("2. show contact")
    print("3. exit")
    choice = input("Enter your choice(1/2/3):")
    if choice == "1":
      while True:
        name = input("Enter contact name:")
        phone_number = input("Enter contact's phone number:")
        contacts.append({"name": name, "phone": phone_number})
        print(f"{name} added successfully.")
        #ask if user wants to add another contact
        add_another = input("Do you want to add another contact?(y/n):").lower()
        if add_another != "y":
          break
    elif choice == "2":
      show_contact()

    elif choice == "3":
     print("bye")
     break
    else:
      print("Invalid choice. Try again.")
