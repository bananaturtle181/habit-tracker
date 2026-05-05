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