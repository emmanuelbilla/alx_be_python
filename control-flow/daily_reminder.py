task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(task + " is a high priority task that requires immediate attention today!")
        else:
            print(task + " is a high priority task. Finish it today!")
    case  "medium":
        if time_bound == "yes":
            print(task + " is a medium priority task. Get it done after today's high priority tasks!")
        else:
            print(task + " is a medium priority task. Find time for it!")
    case "low":
        if time_bound == "yes":
            print(task + " is a low priority task but requires immediate attention today!")
        else:
            print(task + " is a low priority task. Consider completing it when you have free time")
    case _:
        print("You entered one or more wrong values. Recheck them and try again!")
