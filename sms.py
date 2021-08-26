import sqlite3


class Student:
    def __init__(self,roll,first,last,dob,course_id):
        self.conn=sqlite3.connect('college.db')
        self.c=self.conn.cursor()
        self.roll=roll
        self.first=first
        self.last=last
        self.dob=dob
        self.course_id=course_id
        self.c.execute('''CREATE TABLE IF NOT EXISTS students 
                (roll INTEGER PRIMARY KEY ,
                first text,
                last text,
                dob text,
                course_id INTEGER,
                FOREIGN KEY (course_id) REFERENCES courses (course_id))''')
        
    def add_student(self):
        try:
            self.c.execute('''INSERT INTO students VALUES (?, ?, ?, ?, ?)''',(self.roll, self.first, self.last, self.dob, self.course_id))
            self.conn.commit()
            print('You have sucessfully registered')
            self.conn.close()
        except Exception:
           print('ERROR: Could not add to student table')
    
   


class Course:
    def __init__(self,course_id,course_name,duration,fees):
        self.conn=sqlite3.connect('college.db')
        self.c=self.conn.cursor()
        self.course_id=course_id
        self.course_name=course_name
        self.duration=duration
        self.fees=fees
        self.c.execute('''CREATE TABLE IF NOT EXISTS courses
                    (course_id INTEGER PRIMARY KEY,
                    course_name text,
                    duration INTEGER,
                    fees INTEGER)''')

    def add_course(self):
        try:    
            self.c.execute('''INSERT INTO courses(course_id,course_name,duration,fees) VALUES (?,?,?,?)''',(self.course_id,self.course_name,self.duration,self.fees))
            self.conn.commit()
            print('Sucessfully added course')
            self.conn.close()
        except Exception:
            print('ERROR: could not add to courses table')
    
def view_table_students():
    conn=sqlite3.connect('college.db')
    c=conn.cursor()
    c.execute("SELECT * FROM students")
    rows=c.fetchall()
    for row in rows:
        print(row)
    conn.close()
    
def view_table_courses():
    conn=sqlite3.connect('college.db')
    c=conn.cursor()
    c.execute("SELECT * FROM courses")
    rows=c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def apply_to_course(roll,course_id):
    conn=sqlite3.connect('college.db')
    c=conn.cursor()
    c.execute('''UPDATE students SET course_id = ? WHERE roll = ?''',(course_id,roll))
    conn.commit()
    print('Successfully updated the course')
    conn.close()
    #except Exception:
     #   print('there war a problem updating')



if __name__=="__main__":
    print("Welcome to SMS (Student Managment System)")
    print('\nTell us who you are :\n 1.Student\n 2.Admin\n')
    choice=int(input('Enter your choice :')) 

    if(choice==1):
        print('Welcome Student')
        print('Choose what to do')
        print('\n1.Register \n2.View courses \n3.Apply for course')
        choice = int(input())

        if (choice==1):
            print('Enter your Roll number : ')
            roll_num=int(input())
            print('Enter your first name :')
            first_name = input()
            print('Enter your last name : ')
            last_name = input()
            print('Enter your Date of Birth : ')
            DOB = input()
            print('Enter the course ID : ')
            Course_id=int(input())
            student = Student(roll_num,first_name,last_name,DOB,Course_id)
            student.add_student()

        elif(choice==2):
            view_table_courses()

        elif(choice==3):
            roll=int(input('Enter your roll : \n'))
            course_id=int(input('Enter the new course ID : \n'))
            apply_to_course(roll,course_id)

        
        else:
            print('Inncorrect choice,Student. Try again')


    elif(choice==2):
        print('Welcome Admin')
        print('tell us what to do\n 1.Add a new course to the list \n 2.View all students table\n 3.view all Courses table')
        choice=int(input('tell us your choice Admin \n'))
        if(choice==1):
            print('Enter the Course ID : ')
            course_id=int(input())
            print('Enter the Course name :')
            course_name = input()
            print('Enter the course duration : ')
            duration = input()
            print('Enter the fees for the course : ')
            fees = int(input())
            course=Course(course_id,course_name,duration,fees)
            course.add_course()
        elif(choice==2):
            view_table_students()
        elif(choice==3):
            view_table_courses()
        else:
            print('Incorrect choice, Admin. Try again')            


    else:
        print('Incorrect choice, User. Try again')