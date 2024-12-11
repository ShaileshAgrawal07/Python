#Add two numbers
def addition(number_1,number_2):
    result = number_1 + number_2
    return result

#Multipliy two numbers
def multiplication(number_1,number_2):
    result = number_1 * number_2
    return result

number_1 = int(input("Enter first number "))
number_2 = int(input("Enter second number "))
addition = addition(number_1,number_2)
print("The sum of two numbers is", addition)
Multiply = multiplication(number_1,number_2)
print("The multiplication of two numbers is", Multiply)