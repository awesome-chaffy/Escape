# def maydays(Mayday):
  # mission_control_message = ""
  # for problem in range(3):
    # print(f"Mayday! {Mayday})
  # if Mayday = "Fuel tank broken":
    # print(Mission_control_message)


def problem(mayday):
    known_maydays = [
    "system failure",
    "hatch unsealable",
    "thruster failure",
    "other"
    ]
    if mayday.lower() in known_maydays:
        for i in range(3):
            print("Mayday!")
        print(f"{mayday}!")
    else:
        print("Land the soonest possible!")

our_error = input("What is your problem? ")
problem(our_error)
