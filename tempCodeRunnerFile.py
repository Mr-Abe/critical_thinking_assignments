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
    
    def add(self, a, b):
        print(f'The total from adding {a} to {b} is: {a + b}.')
    
    def subtract(self, a, b):
        print(f'The total for subtracting {b} from {a} is: {a - b}.')
    
    def multiply(self, a, b):
        print(f'The total for multiplying {a} by {b} is: {a * b}.')
    
    def divide(self, a, b):
        if b == 0:
            print('Dividing by 0 results in undefined.')
            return
        
        print(f'The result of dividing {a} by {b} is: {a // b}.')
    



if __name__ == '__main__':
    num_1 = 20 # int(input('Enter the first whole number: '))
    num_2 = 0 # int(input('Enter the second whole number: '))

    myCalculator = Calculator()

    print('Part 1 - Addition and Subtraction', end='\n')
    print('******************************************')
    myCalculator.add(num_1, num_2)
    myCalculator.subtract(num_1, num_2)
    print('Thank you for using this calculator', end='\n\n\n')


    print('Part 2 - Multiplication and Divison')
    print('******************************************')
    myCalculator.multiply(num_1, num_2)
    myCalculator.divide(num_1, num_2)
    print('Thank you for using this calculator', end='\n\n\n')