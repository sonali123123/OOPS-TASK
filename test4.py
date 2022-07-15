# 10 example on protected
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)

class ineuron1:
    def __init__(self,course):
        try:
            self._course = course
        except Exception as e:
            print(e)
obj1 =ineuron1("FSDS")
print(obj1._course)

class ineuron2:
    def __init__(self,coursetype):
        try:
            self._coursetype = coursetype
        except Exception as e:
            print(e)
obj2 = ineuron2("Job Guarantee")
print(obj2._coursetype)

class ineuron3:
    def __init__(self,project1):
        try:
            self._project1 = project1
        except Exception as e:
            print(e)
obj3 = ineuron3("Object Detection")
print(obj3._project1)

class ineuron4:
    def __init__(self,project2):
        try:
            self._project2 = project2
        except Exception as e:
            print(e)

obj4= ineuron4("Whether prediction")
print(obj4._project2)

class ineuron5:
    def __init__(self,internship):
        try:
            self._internship = internship
        except Exception as e:
            print(e)
obj5 = ineuron5("Big Data")
print(obj5._internship)

class ineuron6:
    def __init__(self,course2):
        try:
            self._course2 = course2
        except Exception as e:
            print(e)
obj6 = ineuron6("Deep Learning")
print(obj6._course2)

class ineuron7:
    def __init__(self,course3):
        try:
            self._course3 = course3
        except Exception as e:
            print(e)
obj7 = ineuron7("Machine Learning")
print(obj7._course3)

class ineuron8:
    def __init__(self,course4):
        try:
            self._course4 = course4
        except Exception as e:
            print(e)
obj8 = ineuron8("NLP")
print(obj8._course4)

class ineuron9:
    def __init__(self,course5):
        try:
            self._course5 = course5
        except Exception as e:
            print(e)
obj9 = ineuron9("Statistic")
print(obj9._course5)

class ineuron10:
    def __init__(self,course6):
        try:
            self._course6 = course6
        except Exception as e:
            print(e)
obj10 = ineuron10("Big Data")
print(obj10._course6)