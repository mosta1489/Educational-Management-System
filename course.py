from random import *
import sqlite3
import os
from student import *
from assignment import *


os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Course:

    def __init__(self, doctor_id, name=None):
        self.name = name
        self.doc_id = doctor_id
        self.db = sqlite3.connect("data.db")
        self.cr = self.db.cursor()

    def commit(self):
        self.db.commit()
        self.db.close()

    def create_course(self):

        ID = self.name[:2] + ''.join(str(randrange(1000)))
        self.cr.execute(f"insert into course value ({self.name}, {ID}, {self.doc_id}, {0}, {0})")

    def get_info(self):
        self.cr.execute("select * from Courses where name = self.name")
        info = self.cr.fetchall()
        data = []
        return (
            data.append(i for i in info[0])
        )

    def create_assignment(self):
        pass




if __name__ == "__main__":
    m = Course("mostafa")

