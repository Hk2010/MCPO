def convert_base(num, base):
    """
    Convert a number to another base.
    """
    if base < 2 or base > 16:
        return "Invalid base."

    digits = "0123456789ABCDEF"
    stack = []
    while int(num) > 0:
        rem = int(num) % base
        stack.append(digits[rem])
        num = int(num) // base

    result = ""
    while stack:
        result += stack.pop()

    if '.' in str(num):
        result += '.'
        num = float(num) - int(num)
        for i in range(4):
            num *= base
            result += digits[int(num)]
            num -= int(num)

    return result

# Get the input from the user
num = input("Enter a number: ")
base_from = int(input("Enter the base of the number (2-16): "))
base_to = int(input("Enter the base to convert to (2-16): "))

# Convert the number to decimal first
if '.' in num:
    integer, fraction = num.split('.')
    decimal_num = int(integer, base_from) + sum(int(digit, base_from) / base_from**(i+1) for i, digit in enumerate(fraction))
else:
    decimal_num = int(num, base_from)

# Convert the decimal number to the desired base
result = convert_base(decimal_num, base_to)

# Print the result
print(f"{num} (base {base_from}) = {result} (base {base_to})")
