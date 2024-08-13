from Calculator import Calculator
'''
Part 2:

Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, 
multiply them together to find the output. Also, divide num1/num2 to find the output.

Compile and submit your pseudocode, source code, and screenshots of the application 
executing the code from parts 1 and 2, the results and GIT repository in a single document (Word is preferred).
'''

if __name__ == '__main__':
    num_1 = int(input('Enter the first whole number: '))
    num_2 = int(input('Enter the second whole number: '))

    myCalculator = Calculator()

    print('Part 2 - Multiplication and Divison')
    print('******************************************')
    myCalculator.multiply(num_1, num_2)
    myCalculator.divide(num_1, num_2)
    print('Thank you for using this calculator')