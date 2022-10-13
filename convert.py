number_as_string = input("Enter a decimal number:")


# input() gives us text, let's convert it to number
number = int(number_as_string)

# here we gather the result
result = ""

while number > 0:
    remainder = number % 2
    result = str(remainder) + result
    number = number // 2

print("Result in binary:", result)
print("hello nathan from the popular tv show nathan")
