def welcome():
    print("====== PYTHON LEARNING ASSISTANT ======")
    print("Welcome! Learn Python step by step.")

    name = input("What is your name? ")
    while name == "":
        print("Name cannot be empty.")
        name = input("Please enter your name: ")
    print("welcome", name)    

welcome()

def learn_python():
    print("\n========== PYTHON TOPICS ==========")
    topics = {
        "1": "Introduction to Python",
        "2": "Variables",
        "3": "Data Types",
        "4": "Strings",
        "5": "Numbers",
        "6": "Type Conversion",
        "7": "Operators",
        "8": "User Input",
        "9": "Output",
        "10": "Comments"
    }
    for key, value in topics.items():
        print(f"{key}. {value}")

    print("Welcome to Python lessons!")
    topic_choice = input("Enter a topic number to learn: ")
    if topic_choice in topics:
      print("Topic:", topics[topic_choice])

if topic_choice == "1":
    print("\nWhat is Python?")
    print("Python is a high-level programming language.")
    else:
        print("invalid topic number.")    


def display_menu():
    
    choice = None
    while choice != "4":

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
            learn_python()
           
        elif choice == "2":
            print("take a quiz")
           
        elif choice == "3":
            print("view progress")
           
        elif choice == "4":
            print("Goodbye")
           
        else:
            print("Invalid choice. Please select 1-4.")   
           


display_menu()