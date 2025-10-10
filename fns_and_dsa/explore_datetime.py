import datetime from datetime, timedelta, date

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    number_of_days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.timedelta(number_of_days_to_add) + datetime.date.today()
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")