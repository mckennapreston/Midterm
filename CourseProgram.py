"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import CourseClass as c


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    for student in students:
        print(student)

    MyCourse = c.Course("MIS 4322 - Advanced Python", "250309", 4, "open")

    MyStudent1 = c.Course("John", crn, seats, status)
    MyStudent2 = c.Course("James", crn, seats, status)
    MyStudent3 = c.Course("Jill", crn, seats, status)
    MyStudent4 = c.Course("Jack", crn, seats, status)
    MyStudent5 = c.Course("Joanne", crn, seats, status)

    total_seats = 4

    print("Student Name: ", MyStudent1.get_name())
    print("Course Name: ", MyCourse.get_name())
    print("CRN: ", MyCourse.get_crn())
    print("Seats left: ", MyCourse.get_seats())
    print()

    print("Student Name: ", MyStudent2.get_name())
    print("Course Name: ", MyCourse.get_name())
    print("CRN: ", MyCourse.get_crn())
    print("Seats left: ", MyCourse.get_seats())
    print()

    print("Student Name: ", MyStudent3.get_name())
    print("Course Name: ", MyCourse.get_name())
    print("CRN: ", MyCourse.get_crn())
    print("Seats left: ", MyCourse.get_seats())
    print()

    print("Student Name: ", MyStudent4.get_name())
    print("Course Name: ", MyCourse.get_name())
    print("CRN: ", MyCourse.get_crn())
    print("Seats left: ", MyCourse.get_seats())
    print()

    if MyCourse.get_crn() == MyStudent1.get_crn():
        total_seats -= 1
    if MyCourse.get_crn() == MyStudent2.get_crn():
        total_seats -= 1
    if MyCourse.get_crn() == MyStudent3.get_crn():
        total_seats -= 1
    if MyCourse.get_crn() == MyStudent4.get_crn():
        total_seats -= 1
    if MyCourse.get_crn() == MyStudent5.get_crn():
        total_seats -= 1

    if seats == 0:
        print(
            "Sorry",
            MyStudent5.get_name(),
            "registration is closed for MIS 4322 - Advanced Python.",
        )


main()
