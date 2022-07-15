# 10 examples on method overridding
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)
class Courses1:
    def show(self):
        try:
            print("print the name of students who are enrolled for FSDS course")
        except Exception as e:
            print(e)
class Courses2(Courses1):
    def show(self):
        try:
            print("print the name of students who are enrolled for FSDA  course")
        except Exception as e:
            print(e)
obj1 = Courses1()
obj2 = Courses2()
obj1.show()
obj2.show()
class Courses3:
    def show1(self):
        try:
            print("print the name of students who are enrolled for FSWD  course")
        except Exception as e:
            print(e)
class Courses4(Courses3):
    def show1(self):
        try:
            print("print the students name from FSDS batch who has completed python project")
        except Exception as e:
            print(e)
obj3 = Courses3()
obj4 = Courses4()
obj3.show1()
obj4.show1()
class Courses5():
    def show2(self):
        try:
            print("print the name of students from FSDA batch who has completed time series project")
        except Exception as e:
            print(e)
class Courses6(Courses5):
    def show2(self):
        try:
            print("print the name of students from FSWD batch who has completed project on E-Commerce")
        except Exception as e:
            print(e)
obj5 = Courses5()
obj6 = Courses6()
obj5.show2()
obj6.show2()
class Courses7:
    def show3(self):
        try:
            print("print the name of students from FSDS batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
class Courses8(Courses7):
    def show3(self):
        try:
            print("print the name of students from FSDA batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
obj7 = Courses7()
obj8 = Courses8()
obj7.show3()
obj8.show3()
class Courses9:
    def show4(self):
        try:
            print("print the name of students from FSWD batch who has started internship after their first project completion")
        except Exception as e:
            print(e)
class Courses10(Courses9):
    def show4(self):
        try:
            print("print the name of students from FSDS,FSDA,FSWD batches who got placed in the placement drive at ineuron.ai")
        except Exception as e:
            print(e)
obj9 = Courses9()
obj10 = Courses10()
obj9.show4()
obj10.show4()
