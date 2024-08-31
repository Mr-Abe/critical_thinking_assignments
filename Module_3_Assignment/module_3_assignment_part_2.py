'''
Part 2:

Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. Ask the user for 
the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
'''

def getInputHoursOnly():
    curr_hours = int(input('What is the current time now in hours (0-23)? '))
    
    while curr_hours < 0 or curr_hours > 23:
        print("Please enter a valid time between 0 and 23.")
        curr_hours = int(input('What is the current time now in hours (0-23)? '))

    hours_till_alarm = int(input('Please provide the number of hours to wait until the alarm: '))

    return curr_hours, hours_till_alarm

def getInputHoursAndMinutes():
    curr_hours = int(input('What is the current time now in hours (0-23)? '))
    
    while curr_hours < 0 or curr_hours > 23:
        print("Please enter a valid time between 0 and 23.")
        curr_hours = int(input('What is the current time now in hours (0-23)? '))

    curr_minutes = int(input('What are the current minutes (0-59)? '))
    
    while curr_minutes < 0 or curr_minutes > 59:
        print("Please enter a valid number of minutes between 0 and 59.")
        curr_minutes = int(input('What are the current minutes (0-59)? '))

    hours_till_alarm = int(input('Please provide the number of hours to wait until the alarm: '))
    minutes_till_alarm = int(input('Please provide the number of minutes to wait until the alarm: '))

    return curr_hours, curr_minutes, hours_till_alarm, minutes_till_alarm

def convert_2_24_hours_only(curr_hours, hours_till_alarm):
    alarm_time = (curr_hours + hours_till_alarm) % 24
    return alarm_time

def convert_2_24_hours_and_minutes(curr_hours, curr_minutes, hours_till_alarm, minutes_till_alarm):
    total_minutes = curr_minutes + minutes_till_alarm
    additional_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    total_hours = (curr_hours + hours_till_alarm + additional_hours) % 24

    return total_hours, final_minutes

if __name__ == '__main__':
    print('''Welcome to Scharmy Alarmy! Please choose an option:
    1. Use hours only
    2. Use hours and minutes''')

    choice = input('Enter 1 or 2: ')

    if choice == '1':
        curr_hours, hours_till_alarm = getInputHoursOnly()
        alarm_hours = convert_2_24_hours_only(curr_hours, hours_till_alarm)
        print(f'The alarm will go off at {alarm_hours:02}:00 hours.')

    elif choice == '2':
        curr_hours, curr_minutes, hours_till_alarm, minutes_till_alarm = getInputHoursAndMinutes()
        alarm_hours, alarm_minutes = convert_2_24_hours_and_minutes(curr_hours, curr_minutes, hours_till_alarm, minutes_till_alarm)
        print(f'The alarm will go off at {alarm_hours:02}:{alarm_minutes:02} hours.')
    
    else:
        print('Invalid choice. Please restart the program and choose either 1 or 2.')
