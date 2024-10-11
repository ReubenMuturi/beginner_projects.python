def show_menu():
    print("""Welcome to Text Adventure Game!
    Collect 3 items to win the game, or be eaten by the monster.
    Move commands: go North, go South, go East, go West
    Add to Inventory: get 'item name
        """)
show_menu()

def show_instr():
    print("""Input 'go either, east, west, south, north' to navigate the diff rooms
    Input 'get item' to collect items in the rooms
    If you pick a wrong item, game over!
        """)
show_instr()

def show_status():
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("---------------------------")

rooms = {
    'Hall': {'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'},
    'Dinning': {'west': 'Hall', 'south': 'Garden', 'item': 'potion'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Garden': {'north': 'Dining Room', 'item': 'sword'}
        }

inventory = []
current_room = "Hall"


while True:
    show_status()
    move = input("> ").split()

    if len(move) == 2:
        command, direction = move
        if command.lower() == "go":
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                if "item" in rooms[current_room] and rooms[current_room]['item'] == 'monster':
                    print("A monster has got you... GAME OVER!")
                    break
            else:
                print("You can't go that way!")

        elif command.lower() == "get":
            item = direction
            if "item" in rooms[current_room] and rooms[current_room]['item'] == item:
                inventory.append(item)
                print(f"{item} got!")
                del rooms[current_room]['item']
            else:
                print(f"Can't get {item}!")

        if len(inventory) == 3:
            print("You have collected all items... YOU WIN!")
            break
        else:
            print("Invalid input.")

