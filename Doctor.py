from course import *
import sqlite3
import os
import string
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Doctor:

    def __init__(self, first_name=None, last_name=None):

        self.first_name = first_name
        self.last_name = last_name

        self.db = sqlite3.connect("data.db")
        self.cr = self.db.cursor()

    def create_doctor(self):
        letters = string.ascii_lowercase
        ID = ''.join(str(randrange(100)) for i in range(2))
        user_name = self.first_name[:3] + ''.join(str(randrange(10000)))  # join function take string only
        password = ''.join(random.choice(letters) for i in range(2)) + ''.join(str(randrange(100)) for i in range(2))
        self.cr.execute(
            f"insert into Doctors values('{ID}', '{self.first_name} {self.last_name}', '{user_name}', '{password}' )")
        self.commit_close()

    def commit_close(self):  # function to commit and close data base
        self.db.commit()
        self.db.close()

    def show_doctor_data(self, ID):
        self.cr.execute(f"select * from Doctors where id = {ID}")
        doc_data = self.cr.fetchall()
        data = []
        return (
            data.append(i for i in doc_data[0])
        )

    def create_course(self, course_name, doc_id):
        self.cr.execute("select id from Doctors")
        ids = self.cr.fetchall()
        for i in ids:
            if doc_id in i:
                # new_course = Course(course_name)  # create object from Courses
                break

    def create_assignment(self):
        pass



if __name__ == "__main__":
    mo = Doctor()
    # mo.create_doctor()
    print(mo.show_doctor_data(7918))
