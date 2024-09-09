'''
M (Match): Create a Customer class with two attributes:

    book_purchases: The number of books purchased by the customer.
    points: The number of points earned, calculated based on the purchases.

Include methods to:

    Add books to the customer's purchase history.
    Calculate and return the points based on the number of books purchased.
'''


class Customer:
    def __init__(self, book_purchases=0):
        self.book_purchases = book_purchases
        self.points = 0
    
    def calculate_points(self):
        if self.book_purchases >= 8:
            self.points = 60
        elif self.book_purchases >= 6:
            self.points = 30
        elif self.book_purchases >= 4:
            self.points = 15
        elif self.book_purchases >= 2:
            self.points = 5
        else:
            self.points = 0
        return self.points
    
    def update_purchases(self, purchases):
        self.book_purchases = purchases
        self.calculate_points()
    
    def display_points(self):
        print(f"You purchased {self.book_purchases} books and earned {self.points} points.")
        