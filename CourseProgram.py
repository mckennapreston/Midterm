"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""
from CourseClass import RegisterClass as r
import CourseClass as c


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    MyCourse = c.Course("MIS 4322 - Advanced Python", "250309", 4, "open")

    MyStudent1 = c.Course("John")
    MyStudent2 = c.Course("James")
    MyStudent3 = c, Course("Jill")
    MyStudent4 = c.Couse("Jack")
    MyStudent5 = c.Course("Joanne")

    total_seats = 4

    print("Student Name: ", MyStudent1.get_name())
    print("Course Name: ", MyCourse.get_name())
    print("CRN: ", MyCourse.get_crn())
    print("Seats left: ", MyCourse.get_seats())

    if seats == 0:
        print(
            "Sorry",
            MyStudent5.get_name(),
            "registration is closed for MIS 4322 - Advanced Python.",
        )


main()
