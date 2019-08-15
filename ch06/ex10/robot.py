from laser import Laser
from claw import Claw
from smartPhone import SmartPhone


class Robot():
    def __init__(self):
        self.__laser = Laser()
        self.__claw = Claw()
        self.__smartPhone = SmartPhone()

    def does(self):
        print('robot can do %s, %s and %s' % (self.__laser.does(),
                                              self.__claw.does(), self.__smartPhone.does()))
