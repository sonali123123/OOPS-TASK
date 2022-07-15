#  Examples on abstraction
import test3
print(test3)
obj2 = test3.ineuron3()
print(obj2.project())
import test2
print(test2)
obj1 = test2.Courses()
print(obj1.FSDS_course())
import test5
print(test5)
obj = test5.ineuron1("FSDA")
print(obj._ineuron1__course)
import logging
logging.basicConfig(filename="Lists.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
class ineuron2:
    logging.info("we are under ineuron2 class")
    def __init__(self,project,internship):
        logging.info("We are under the function of class ineuron2")
        try:
            self._project1 = project
            self.__internship1 = internship
        except Exception as e:
            logging.exception(e)
sonali = ineuron2("Object detection","doing internship from ineuron internship portal on BIG DATA")
print(sonali._project1)
print(sonali._ineuron2__internship1)


