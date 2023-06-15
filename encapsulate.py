
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)


class Protected2:
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected2()
obj._protectedVar = 34
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

class both:
    def __init__(self):
        self._bothVar = 0
        self._bothVar = 12

    def getboth(self):
        print(self.__bothVar)

    def setboth(self, private):
        self._privateVar = both

obj = both()
obj.getboth()
obj.setboth(12)
obj.getboth()

