def players():
    players = []

    while True:
        try:
            no_players = int(input("How many players are playing?"))
            confirm = input(f"There are going to be {no_players} playing. Is that correct?(y/n)")

            if confirm in ("y", "Y"):
                for i in range(1,no_players + 1):
                    player = {'name': input(f"What is player {i}'s name? ")
                    }
                break

            else: continue

        except ValueError:
            print("Please provide a valid whole number")

    
    
    return

players()
