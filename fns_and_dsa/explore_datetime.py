import datetime

def display_current_datetime():
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    print(f"Current date and time: {current_date}:{current_time}")

def calculate_future_date():
    number_of_days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.timedelta(number_of_days_to_add) + datetime.date.today()
    print(f"Future date: {future_date}")