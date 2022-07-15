# 10 examples on public (3 example on 1st class, 3 example on 2nd class, 4 example on 3rd class)
import logging
logging.basicConfig(filename="inheritence.log",level=logging.DEBUG)
class ineuron1:
    def __init__(self):
        self.course1 = "FSDS"
    def course(self):
        try:
            print(self.course1)
        except Exception as e:
            print(e)
o = ineuron1()
o.course()
o.course1="FSDA"
o.course()
o.course1="FSWD"
o.course()
o.course1 = "Community Classes"
o.course()


class ineuron2:
    def __init__(self):
        self.students1= "data science"

    def students(self):
        try:
            print(self.students1)
        except Exception as e:
            print(e)
i = ineuron2()
i.students()
i.students1="data analytics"
i.students()
i.students1 = "web development"
i.students()
i.students1 = "Cyber Security"
i.students()

class ineuron3:
    def __init__(self):
        self.project1 = "Data Visualisation"
    def project(self):
        try:
            print(self.project1)
        except Exception as e:
            print(e)
p = ineuron3()
p.project()
p.project1 = "E-commerce"
p.project()
p.project1 = "Object detection"
p.project()
p.project1 = "web scrapping"
p.project()
p.project1 = "time series"
p.project()

