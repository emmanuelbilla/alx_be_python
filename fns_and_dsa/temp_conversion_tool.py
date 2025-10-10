FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp_in_celsius}°C")

def convert_to_fahrenheit(celsius):
    temp_in_fahrenheit = celsius* CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celsius}°C is {temp_in_fahrenheit}°F")

temp_to_convert = float(input("Enter the temperature to convert: "))
scale = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
converted =False

while converted == False:
    if scale.upper() == "C":
        convert_to_fahrenheit(temp_to_convert)
        converted = True
    
    elif scale.upper() == "F":
        convert_to_celsius(temp_to_convert)
        converted = True
    
    else:
        print("Check your input.")

