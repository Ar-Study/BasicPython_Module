# Termometer / Konversi Suhu


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_reamur(celsius):
    return celsius * 4/5

def main():
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    print(f"{celsius} derajat Celsius = {celsius_to_fahrenheit(celsius)} derajat Fahrenheit")
    print(f"{celsius} derajat Celsius = {celsius_to_kelvin(celsius)} derajat Kelvin")
    print(f"{celsius} derajat Celsius = {celsius_to_reamur(celsius)} derajat Reamur")

if __name__ == "__main__":
    main()
