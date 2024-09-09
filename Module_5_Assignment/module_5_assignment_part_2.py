'''
Part 2:

The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 
The points are awarded as follows:

    If a customer purchases 0 books, they earn 0 points.
    If a customer purchases 2 books, they earn 5 points.
    If a customer purchases 4 books, they earn 15 points.
    If a customer purchases 6 books, they earn 30 points.
    If a customer purchases 8 or more books, they earn 60 points.

Write a program that asks the user to enter the number of books that they have purchased this month and then display the 
number of points awarded.

U - number of purchases converts to points gained by each customer
M - Class customer with book_purchase attribute and points attribute.  with methods for book purchase that tracks points
P - Use OOP and the appropriate principles, utilize the necessary operators and expressions that make sense.
'''
from Customer import Customer


def get_purchase_count():
    while True:
        try:
            purchases = int(input("Enter the number of books you purchased this month: "))

            if purchases < 0:
                print("Please enter a non-negative number.")
            else:
                return purchases
        except ValueError:
            print(f'{purchases} is invalid, please enter a numerical digit equal to or larger than zero: ') 


def main():
    
    purchases = get_purchase_count()
    
    customer = Customer()
    customer.update_purchases(purchases)
    
    
    customer.display_points()


if __name__ == "__main__":
    main()

