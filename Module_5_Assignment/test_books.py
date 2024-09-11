from Customer import Customer

def simulate_user_interaction():
    # Define a list of test cases with the expected number of books purchased
    test_cases = [0, 2, 4, 6, 8, 10, -1]  # Including a negative case for robustness

    # Create a Customer instance
    customer = Customer()

    # Loop through each test case
    for books in test_cases:
        print("\n---\n")  # Print a divider for clarity in the output
        print(f"Simulating purchase for {books} books:")
        try:
            customer.update_purchases(books)
            customer.display_points()
        except Exception as e:
            print(f"Error: {str(e)}")  # Print any errors that occur

if __name__ == "__main__":
    simulate_user_interaction()
