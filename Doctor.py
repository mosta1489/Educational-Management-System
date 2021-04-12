
from  course import *
import sqlite3
import os
import string
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Doctor:

    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        self.db = sqlite3.connect("data.db")   # connect to data base
        self.cr = self.db.cursor()   # cursor 

    def commit_close(self): # function to commit and close data base
        self.db.commit()
        self.db.close()

    def createUser(self):   # create random ID and userName and password 

        letters = string.ascii_lowercase     # select all latters lower
        userName = self.FirstName + ''.join(str(randrange(10000)))   # join function take string only
        password = ''.join(random.choice(letters) for i in range(3)) + ''.join(str(randrange(100)) for i in range(2)) 
        ID = ''.join(str(randrange(1000)) for i in range(2))

        # stor data in data base
        self.cr.execute(f"insert into Doctors values('{ID}', '{self.FirstName} {self.LastName}', '{userName}', '{password}' )")
        self.commit_close() # call function to commit and close db

        return (ID, userName, password)   # return tuble has data to show 

    def showData(self):
        data = self.createUser()
        print (f"hello Dr/{self.FirstName} \n your ID is >> {data[0]} \n your UserNme is >> {data[1]} \n your password is >> {data[2]}")

    def CreateCourse(self, courseName):
        newCorse = Course(courseName)   #create object from Courses
        self.cr.execute(f"insert into Courses values('{courseName}','{newCorse.getID()}', '{self.FirstName}', '{[]}')")
        self.commit_close()

    def CreateAssignment(self):
        pass

    def SetGreate(self):
        pass



if __name__ == "__main__":
    mo = Doctor("mostafa","ahmed")
    mo.CreateCourse("graphics")