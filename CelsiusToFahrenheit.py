def celcToF():
    try:
        celc = int(float(input("Enter a Celcius degree:\n")))
        farenhite = (celc * 9 / 5) + 32
        print("Your Farenhite degree is:")
        print(farenhite)
    except ValueError:
        print("Don't enter text!")

User_input = ""
while User_input != "done":
    celcToF()
