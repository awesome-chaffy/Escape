def mayday(mayday):
    maydays = {"system failure": "use emergency power","food supply empty": "order food package","thruster breakdown":
    "use emergency power"}
    if mayday.lower() in maydays:
        for problem in range(3):
            print("Mayday!")
        print(mayday)
    else:
        print("tell mission_control")
    problem = input("What is the problem? ")
