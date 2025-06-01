Task = input("Input task description: ")
Priority = input("Task's Priority, (high,medim or low): ")
Time_bound = input("Is task time bound, (yes or no): ")
match priority:
    case "high":
        print("This is a high priority project")
    case "medium":
        print("This is a medium priority project")
    case "low":
        print("This is a low priority project")
if time_bound == "yes" and priority == "high":
    print(f"{task} is a high priority task that requires immediate attention today.")
if time_bound == "no" and priority == "low":
    print(f"{task} is a low priority task. Consider completing it when you have free time")
else:
    print("Please classify your task time bounds")
