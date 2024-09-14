"""
This program stores course information (room number, instructor, meeting time) in dictionaries.

The program should let the user enter a course number and then it should display 
the course's room number, instructor, and meeting time.

Key-value pairs for the dictionaries are as follows:

Course-Room Dictionary:
- 'CSC101': 3004
- 'CSC102': 4501
- 'CSC103': 6755
- 'NET110': 1244
- 'COM241': 1411

Course-Instructor Dictionary:
- 'CSC101': 'Haynes'
- 'CSC102': 'Alvarado'
- 'CSC103': 'Rich'
- 'NET110': 'Burke'
- 'COM241': 'Lee'

Course-Meeting Time Dictionary:
- 'CSC101': '8:00 a.m.'
- 'CSC102': '9:00 a.m.'
- 'CSC103': '10:00 a.m.'
- 'NET110': '11:00 a.m.'
- 'COM241': '1:00 p.m.'

U - create a dictionaries to store and retrieve the course specific details. So when the user enters a course
    they receive that course's instructor, room, and meeting time.
M - Dictionaries
    Use 3 dictionaries with courses as keys and instructor, room, meeting times as values respectively to store the information.
    prompt the user for course number
    if course number is found return instructor, room, and meeting time
P - initialize three dictionaries instructor{}, room{}, meeting_time{}
    prompt the user for a course
    search if course key is in all three dictionaries
        if it is
            retrieve all values
        if not
            display error message
    print information to output
I
R
E
"""
def get_course_info(course_number, course_dicts):
    """
    Retrieves course information based on the provided course number from the dictionaries.
    
    Args:
    course_number (str): The course number to look up.
    course_dicts (dict): A dictionary containing dictionaries for room, instructor, and time.
    
    Returns:
    tuple: Contains room number, instructor, and meeting time if course is found, otherwise returns an error message.
    """
    room_dict, instructor_dict, meeting_time_dict = course_dicts
    try:
        room = room_dict[course_number]
        instructor = instructor_dict[course_number]
        meeting_time = meeting_time_dict[course_number]
        return room, instructor, meeting_time
    except KeyError:
        return None, f"Error: Course \'{course_number}\' not found."

def display_course_info(course_number, course_info):
    """
    Displays the course information or an error message.
    
    Args:
    course_number (str): The course number.
    course_info (tuple): Contains course details or an error message.
    """
    if course_info[0]:
        room, instructor, meeting_time = course_info
        print(f"Course: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print(course_info[1])

def main():
    """
    Main function to run the program logic.
    """
    course_room = {
        'CSC101': 3004,
        'CSC102': 4501,
        'CSC103': 6755,
        'NET110': 1244,
        'COM241': 1411
    }

    course_instructor = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    course_meeting_time = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }
    
    course_dicts = (course_room, course_instructor, course_meeting_time)
    
    while True:
        course_number = input("Enter the course number (e.g., CSC101) or type 'exit' to quit: ")
        if course_number.lower() == 'exit':
            print("Exiting the program. Thank you for using it!")
            break
        course_number = course_number.upper()
        course_info = get_course_info(course_number, course_dicts)
        display_course_info(course_number, course_info)
        print("|-------------------------------|")

if __name__ == '__main__':
    main()