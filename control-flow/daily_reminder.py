Task = input("Enter your task: ")
Time_bound = input("Is it time_bound, (yes or no): ")
Priority = input("Priority, (high/medim/low): ")

match Priority:
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
