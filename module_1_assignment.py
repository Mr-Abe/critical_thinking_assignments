'''
Creating Python Programs
Part 1:

Write a Python program to find the addition and subtraction of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, 
add them together to find the output. Also, subtract the two numbers to find the output.


Part 2:

Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, 
multiply them together to find the output. Also, divide num1/num2 to find the output.

Compile and submit your pseudocode, source code, and screenshots of the application 
executing the code from parts 1 and 2, the results and GIT repository in a single document (Word is preferred).
'''


class Calculator():
    
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    



if __name__ == '__main__':
    num_1 = int(input('Enter the first whole number: '))
    num_2 = int(input('Enter the second whole number: '))

    myCalculator = Calculator()

    addTotal = myCalculator.addition(num_1, num_2)
    subTotal = myCalculator.subtraction(num_1, num_2)

    print(f'The total from adding your values is: {addTotal}, and the total for subtracting them is: {subTotal}.')
    print('Thank you for using this calculator')