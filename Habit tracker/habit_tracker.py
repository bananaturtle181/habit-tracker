#Initialise habits list
#Example structure: {"name": "Gym", "dates": []}
habits = []

def add_habit():

    name = input("Enter habit name: ")

    habit = {
        "name": name,
        "dates": []
    }
    habits.append(habit)
    print(f"Habit {name} added!")

    return

def view_habits():

    if not habits:
        print("No habits added yet")
    
    for h in habits:
        print(h)

    return

def menu():

    #Print menu items
    while True:
        print("Option 1: Add habit")
        print("Option 2: view habits")

        user_choice = input("What would you like to do? ")

        if user_choice == 1:
            print("You have chosen to add a habit")
            add_habit()

            show_menu = input("Would you like to do anything else? (y/n)")
            
            if show_menu in ("y","Y"):
                continue
            else: break

        if user_choice == 2:
            print("You have chosen to view habits")
            view_habits() 


    return