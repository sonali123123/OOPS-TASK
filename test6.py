# 10 examples on constructor
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)

class ineuron1:
    def __init__(self,course):
        try:
            self.course = course
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course)
        except Exception as e:
            print(e)
o = ineuron1("FSDS")
o.display()

class ineuron2:
    def __init__(self,course1):
        try:
            self.course1 = course1
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course1)
        except Exception as e:
            print(e)
o1 = ineuron2("FSDA")
o1.display()

class ineuron3:
    def __init__(self,course3):
        try:
            self.course3= course3
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course3)
        except Exception as e:
            print(e)
o2 = ineuron3("FSWD")
o2.display()

class ineuron4:
    def __init__(self,course4):
        try:
            self.course4 = course4
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course4)
        except Exception as e:
            print(e)
o3 = ineuron4("NLP")
o3.display()

class ineuron5:
    def __init__(self,course5):
        try:
            self.course5 = course5
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course5)
        except Exception as e:
            print(e)
o4 = ineuron4("CV")
o4.display()

class ineuron6:
    def __init__(self,course6):
        try:
            self.course6 = course6
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course6)
        except Exception as e:
            print(e)
o5 = ineuron4("Deep Learning")
o5.display()

class ineuron7:
    def __init__(self,course7):
        try:
            self.course7 = course7
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course7)
        except Exception as e:
            print(e)
o6 = ineuron7("Machine Learning")
o6.display()

class ineuron8:
    def __init__(self,course8):
        try:
            self.course8 = course8
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course8)
        except Exception as e:
            print(e)
o7 = ineuron8("Statistic")
o7.display()

class ineuron9:
    def __init__(self,course9):
        try:
            self.course9 = course9
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course9)
        except Exception as e:
            print(e)
o8= ineuron8("Big Data")
o8.display()

class ineuron10:
    def __init__(self,course10):
        try:
            self.course10 = course10
        except Exception as e:
            print(e)
    def display(self):
        try:
            print(self.course10)
        except Exception as e:
            print(e)
o9= ineuron9("Python Basic and advanced with My Sql")
o9.display()
