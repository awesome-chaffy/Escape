def mayday(mayday):
    try:
        maydays = {
        "system failure": "use emergency power.",
        "food supply empty": "order food package.",
        "thruster breakdown": "use emergency power.",
        "i need a pee": "use the martian toilets."
        }
        print(maydays[mayday.lower()])
        for problem in range(3):
            print("Mayday!")
        print(mayday)
    except KeyError as e:
        print(f"tell mission control {e}")
problem = input("What is the problem? ")
mayday(problem)
