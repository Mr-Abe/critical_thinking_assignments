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