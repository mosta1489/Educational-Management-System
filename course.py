
from random import *
import sqlite3
from student import *


class Course:

    def __init__(self,name):
        self.name = name
        self.db = sqlite3.connect("data.db")
        self.cr = self.db.cursor()

    def commit(self):
        self.db.commit()
        self.db.close()

    def getID(self):
        ID = self.name[:2] + ''.join(str(randrange(10000)))

        return ID

    def SetStudent(self,student):
        self.cr.execute("insert into")
        

        pass



if __name__ == "__main__":
    m = Course("mostafa")
    print(m.getID())