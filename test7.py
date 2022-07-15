#  examples on abstraction

import test8
print(test8)
obj=test8.ineuron2("Data Visualisaion","Not started yet!!")
print(obj._project1)
print(obj._ineuron2__internship1)



import logging
logging.basicConfig(filename="Lists.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

class ineuron1:
    logging.info("We are in ineuron1 class")
    def __init__(self,name,course):
        logging.info("We are under the function of ineuron1 class")
        try:
            self._name1 = name
            self.__course1 = course
        except Exception as e:
            print(e)
sona = ineuron1("Sonali","Full Stack Data Science")
print(sona._name1)
print(sona._ineuron1__course1)

