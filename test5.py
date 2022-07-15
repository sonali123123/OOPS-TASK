# 10 Examples on private
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)

class ineuron1:
    def __init__(self,course):
        try:
            self.__course = course
        except Exception as e:
            print(e)
obj1 =ineuron1("FSDS")
print(obj1._ineuron1__course)

class ineuron2:
    def __init__(self,coursetype):
        try:
            self.__coursetype = coursetype
        except Exception as e:
            print(e)
obj2 = ineuron2("Job Guarantee")
print(obj2._ineuron2__coursetype)

class ineuron3:
    def __init__(self,project1):
        try:
            self.__project1 = project1
        except Exception as e:
            print(e)
obj3 = ineuron3("Object Detection")
print(obj3._ineuron3__project1)

class ineuron4:
    def __init__(self,project2):
        try:
            self.__project2 = project2
        except Exception as e:
            print(e)

obj4= ineuron4("Whether prediction")
print(obj4._ineuron4__project2)

class ineuron5:
    def __init__(self,internship):
        try:
            self.__internship = internship
        except Exception as e:
            print(e)
obj5 = ineuron5("Big Data")
print(obj5._ineuron5__internship)

class ineuron6:
    def __init__(self,course2):
        try:
            self.__course2 = course2
        except Exception as e:
            print(e)
obj6 = ineuron6("Deep Learning")
print(obj6._ineuron6__course2)

class ineuron7:
    def __init__(self,course3):
        try:
            self.__course3 = course3
        except Exception as e:
            print(e)
obj7 = ineuron7("Machine Learning")
print(obj7._ineuron7__course3)

class ineuron8:
    def __init__(self,course4):
        try:
            self.__course4 = course4
        except Exception as e:
            print(e)
obj8 = ineuron8("NLP")
print(obj8._ineuron8__course4)

class ineuron9:
    def __init__(self,course5):
        try:
            self.__course5 = course5
        except Exception as e:
            print(e)
obj9 = ineuron9("Statistic")
print(obj9._ineuron9__course5)

class ineuron10:
    def __init__(self,course6):
        try:
            self.__course6 = course6
        except Exception as e:
            print(e)
obj10 = ineuron10("Big Data")
print(obj10._ineuron10__course6)