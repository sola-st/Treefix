# Extracted from https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
class empDetails:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    @classmethod
    def increment(cls,name,none):
        return cls('yarramsetti',6000 + 500)
    @staticmethod
    def salChecking(sal):
        return sal > 6000

emp1=empDetails('durga prasad',6000)
emp2=empDetails.increment('yarramsetti',100)
# output is 'durga prasad'
print emp1.name
# output put is 6000
print emp1.sal
# output is 6500,because it change the sal variable
print emp2.sal
# output is 'yarramsetti' it change the state of name variable
print emp2.name
# output is True, because ,it change the state of sal variable
print empDetails.salChecking(6500)

