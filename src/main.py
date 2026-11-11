def welcome():
    print("====== PYTHON LEARNING ASSISTANT ======")
    print("Welcome! Learn Python step by step.")

    name = input("What is your name? ")
    while name == "":
        print("Name cannot be empty.")
        name = input("Please enter your name: ")
    print("welcome", name)    

welcome()

def display_menu():
    print("\n========== MAIN MENU ==========")
    menu = {
        "1": "learn python",
        "2": "take a quiz",
        "3": "view progress",
        "4": "exit"
    }
    for key, value in menu.items():
        print(f"{key}. {value.title()}")

    choice = input("enter your choice (1-4):")
    print("You selected:", choice)

    if choice == "1":
        print("let learn python")
    elif choice == "2":
        print("take a quiz")
    elif choice == "3":
        print("view progress")
    elif choice == "4":
        print("Goodbye")
    else:
        print("Invalid choice. Please select 1-4.")   
            


display_menu()