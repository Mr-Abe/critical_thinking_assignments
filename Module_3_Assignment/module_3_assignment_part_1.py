'''
Part 1:

Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food and then calculate 
the amounts with an 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total price.

U - given int price find the tip and the tax. tip is 18 percent of the charge. Tax is 7 percent. 
    Both calculated on the charge itself. Return each individual and combined as a total. Output should look nice.
M - create a receipt class and provide methods for calculating tip, tax, as well as providing output.
P
I
R
E
'''

class Receipt():

    def __init__(self, total=0):
        self.total = total
        self.tax = 0
        self.tip = 0

    def calcTax(self):
        self.tax = .07 * self.total
        return self.tax
    
    def calcTip(self):
        self.tip = .18 * self.total
        return self.tip
    
    def calcTotal(self):
        tax = self.calcTax()
        tip = self.calcTip()

        total = self.total + tax + tip
        return total
    
    def printReceipt(self):
        receipt = (f'Charge: ${self.total:.2f}\n'
                   f'Tax: ${self.calcTax():.2f}\n'
                   f'Tip: ${self.calcTip():.2f}\n'
                   f'Total: ${self.calcTotal():.2f}\n')
        print (receipt)
    

if __name__ == '__main__':
    invalid_entry = True
    while invalid_entry:
        try:
            charge = int(input('Enter the charge: '))
            if charge < 0:
                print(f'Charge cannot be negative, you gave: ${charge:.2f}!\n')
            else:
                invalid_entry = False
        except ValueError:
            print('Invalid entry, please provide only numbers!')
            
    print('\n\n')

    receipt = Receipt(charge)
    receipt.printReceipt()
    