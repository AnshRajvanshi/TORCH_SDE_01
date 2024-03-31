def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Converter")
    print("Supported temperature units: Celsius, Fahrenheit, Kelvin")

    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit of measurement (C/F/K): ").upper()

    if unit == 'C':
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit == 'F':
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit == 'K':
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit!")
        return

    print("Converted temperatures:")
    print(f"{celsius:.2f} degrees Celsius")
    print(f"{fahrenheit:.2f} degrees Fahrenheit")
    print(f"{kelvin:.2f} Kelvin")

if __name__ == "__main__":
    main()