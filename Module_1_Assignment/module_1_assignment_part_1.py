from Calculator import Calculator

'''
Creating Python Programs
Part 1:

Write a Python program to find the addition and subtraction of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, 
add them together to find the output. Also, subtract the two numbers to find the output.

'''

if __name__ == '__main__':
    num_1 = int(input('Enter the first whole number: '))
    num_2 = int(input('Enter the second whole number: '))

    myCalculator = Calculator()

    print('Part 1 - Addition and Subtraction', end='\n')
    print('******************************************')
    myCalculator.add(num_1, num_2)
    myCalculator.subtract(num_1, num_2)
    print('Thank you for using this calculator')