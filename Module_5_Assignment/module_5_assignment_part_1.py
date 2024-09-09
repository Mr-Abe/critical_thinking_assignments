'''
Part 1:

Write a program that uses nested loops to collect data and calculate 
the average rainfall over a period of years. 
The program should first ask for the number of years. 
The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, 
and the average rainfall per month for the entire period.

U - two loops, outer loop end condition is based on user input.
    for each iteration the inner loop will fill 12 months with user inputted data.
    output upon completion should be:
                total_months:
                total_inches_rain:
                avg_rain_month:
M - two for loops for calculating years.
'''


def get_num_years():
    while True:
        try:
            num_years = int(input('Enter the number of years: '))
            if num_years <= 0:
                print("Number of years must be greater than 0. Please try again.")
            else:
                return num_years
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")


def get_rainfall_data(num_years):
    total_rainfall = 0
    total_months = num_years * 12 
    
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")

        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please try again.")
                    else:
                        total_rainfall += rainfall
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    
    return total_rainfall, total_months


def display_results(total_rainfall, total_months):
    avg_rainfall_per_month = total_rainfall / total_months
    print(f"\nTotal number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {avg_rainfall_per_month:.2f}")


def main():
    num_years = get_num_years()
    total_rainfall, total_months = get_rainfall_data(num_years)
    display_results(total_rainfall, total_months)


if __name__ == '__main__':
    main()