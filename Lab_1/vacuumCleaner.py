rooms = {
    "A": "DIRTY",
    "B": "CLEAN",
    "C": "DIRTY",
    "D": "DIRTY"
}
position = "A"
movement = {
    "A": "B",
    "B": "D",
    "D": "C",
    "C": "A"
}

def vacuum_agent():
    global position
    while "DIRTY" in rooms.values():
        print("\nCurrent position:", position)
        print("Room status:", rooms)
        if rooms[position] == "DIRTY":
            print("Action: SUCK")
            rooms[position] = "CLEAN"
        else:
            print("Action: MOVE")
            position = movement[position]
    print("\nAll rooms are clean!")
    print("Final room status:", rooms)
vacuum_agent()