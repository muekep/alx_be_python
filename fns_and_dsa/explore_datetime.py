from datetme import datetime
def display_current_datetime():
  current_datetime = datetime.datetime.now()
  current_date = current_datetime.date()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current Date and Time: {formatted_datetime}")
def calculate_future_date():
    while True:
        try:
            days_str = input("Enter a number of days (e.g., 7 for one week): ")
            days_to_add = int(days_str)
            if days_to_add < 0:
                print("Please enter a non-negative number of days.")
            else:
                break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get the current date
    current_date = datetime.date.today()

    # Calculate the future date
    # Create a timedelta object with the specified number of days
    time_delta = datetime.timedelta(days=days_to_add)
    future_date = current_date + time_delta

    # Print the future date in "YYYY-MM-DD" format
    print(f"\nIf today is {current_date}, then in {days_to_add} days, the date will be: {future_date.strftime('%Y-%m-%d')}")
