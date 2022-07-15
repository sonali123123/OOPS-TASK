# 10 examples on inheritence
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)
class Courses:
    def FSDS_course(self):
        try:
            print("print the name of students who are enrolled for FSDS course")
        except Exception as e:
            print(e)
    def FSDA_course(self):
        try:
            print("print the name of students who are enrolled for FSDA  course")
        except Exception as e:
            print(e)
    def FSWD_course(self):
        try:
            print("print the name of students who are enrolled for FSWD  course")
        except Exception as e:
            print(e)
class project(Courses):
    def python_project1(self):
        try:
            print("print the students name from FSDS batch who has completed python project")
        except Exception as e:
            print(e)
    def timeSeries_project2(self):
        try:
            print("print the name of students from FSDA batch who has completed time series project")
        except Exception as e:
            print(e)
    def Ecommerce_project3(self):
        try:
            print("print the name of students from FSWD batch who has completed project on E-Commerce")
        except Exception as e:
            print(e)
class internship(project):
    def ineuron_intern1(self):
        try:
            print("print the name of students from FSDS batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
    def ineuron_intern2(self):
        try:
            print("print the name of students from FSDA batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
    def ineuron_intern3(self):
        try:
            print("print the name of students from FSWD batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
class placement(internship):
    def ineuron_placement_drive(self):
        try:
            print("print the name of students from FSDS,FSDA,FSWD batches who got placed in the placement drive at ineuron.ai")
        except Exception as e:
            print(e)
i = placement()
i.ineuron_placement_drive()
i.ineuron_intern3()
i.ineuron_intern2()
i.ineuron_intern1()
i.Ecommerce_project3()
i.timeSeries_project2()
i.python_project1()
i.FSWD_course()
i.FSDA_course()
i.FSDS_course()

