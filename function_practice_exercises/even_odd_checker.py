def check_even(number):
    remainder = number%2 #Use modulo to check if there would be a remainder instead of division.
    if remainder == 0:
        print(f"{number} is even.") #Mod 2 of even numbers would return 0
    else:
        print(f"{number} is odd.") #Mod 2 of odd numbers would return an int

check_even(10)