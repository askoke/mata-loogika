'''
# decimal -> bianry
number_as_string = input("Enter a decimal number:")
#number_as_string = input("tere")

# input() gives us text, let's convert it to number
 number = int(number_as_string)

# here we gather the result
 result = ""

 while number > 0:
     remainder = number % 2
     result = str(remainder) + result
     number = number // 2

 print("Result in binary:", result)
'''
# bianry -> decimal

binary_as_string = input("Enter a binary number:")
binary_count = len(binary_as_string)

decimal_number = 0
pow_value = 0
while(binary_count > 0):
    print(binary_as_string[binary_count-1])
    decimal_number += pow(2, pow_value) * int(binary_as_string[binary_count-1])
    binary_count -= 1
    pow_value += 1

print("Return in decimal: ", decimal_number)