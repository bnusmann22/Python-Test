while True:
    cmd = input("\nCommand (date/time/quit): ").lower()
    if cmd == "quit":
        break
    if not cmd:
        print("Type something!")
        continue
    
    if cmd == "date":
        from datetime import date
        print("Today:", date.today())
    elif cmd == "time":
        from datetime import datetime
        print("Now:", datetime.now().strftime("%H:%M:%S"))
    else:
        print("Unknown command")


year_of_birth = 2005


height_in_metres = 4.56

favourite_color = "blue"

print(f"Year of birth: {year_of_birth}")
print(f"Height in metres: {height_in_metres}")
print(f"Favourite color: {favourite_color}")


current_year = 2025

age = current_year - year_of_birth
print(f"Age: {age}")

total_points = 0

def add_points(points):
    return score + points   