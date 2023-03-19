def validate_number(number, base):
    if base == "Binary":
        valid_chars = set("01")
    elif base == "Octal":
        valid_chars = set("01234567")
    elif base == "Decimal":
        valid_chars = set("0123456789")
    elif base == "Hexadecimal":
        valid_chars = set("0123456789abcdefABCDEF")
    else:
        return False
    
    if set(number) <= valid_chars:
        return True
    else:
        return False

def convert_number(number, base):
    if base == "Binary":
        decimal = int(number, 2)
    elif base == "Octal":
        decimal = int(number, 8)
    elif base == "Decimal":
        decimal = float(number)
    elif base == "Hexadecimal":
        decimal = int(number, 16)
    
    binary = bin(decimal)[2:]
    octal = oct(decimal)[2:]
    hexadecimal = hex(decimal)[2:]
    
    return binary, octal, decimal, hexadecimal

number_systems = ["Binary", "Octal", "Decimal", "Hexadecimal"]
base = input("Choose a number system (Binary, Octal, Decimal, Hexadecimal): ")

if base in number_systems:
    number = input(f"Enter a number in {base} format: ")
    if validate_number(number, base):
        binary, octal, decimal, hexadecimal = convert_number(number, base)
        print(f"Binary: {binary}")
        print(f"Octal: {octal}")
        print(f"Decimal: {decimal}")
        print(f"Hexadecimal: {hexadecimal}")
    else:
        print(f"Invalid {base} number.")
else:
    print("Invalid number system.")
