'''
Part 2:

Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. Ask the user for 
the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
'''

def getInput():
    
    curr_time = int(input('What is the time now in hours (0-23)? '))

    while curr_time < 0 or curr_time > 23:
        print('Please enter a valid time between 0 and 23.')
        curr_time = int(input('What is the time now in hours (0-23)? '))

    hours_till_alarm = int(input('Please provide the number of hours to wait until the alarm: '))
    
    return curr_time, hours_till_alarm

def convert_2_24(curr_time, hours_till_alarm):

    alarm_time = (curr_time + hours_till_alarm) % 24

    return alarm_time


if __name__ == '__main__':
    print('''Welcome to scharmy alarmy, where you can provide the time now and hours until alert. 
          The program will then give you the time of the alarm using a 24 hour clock.''')
    
    curr_time, hours_till_alarm = getInput()

    alarm_time = convert_2_24(curr_time, hours_till_alarm)
    print(f'The alarm will go off at {alarm_time}:00 hours.')