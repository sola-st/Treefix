# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/805066/how-do-i-call-a-parent-classs-method-from-a-child-class-in-python
from l3.Runtime import _l_
class Dog(object):
    _l_(1141)

    name = ''
    _l_(1131)
    moves = []
    _l_(1132)

    def __init__(self, name):
        _l_(1134)

        self.name = name
        _l_(1133)

    def moves_setup(self,x):
        _l_(1138)

        self.moves.append('walk')
        _l_(1135)
        self.moves.append('run')
        _l_(1136)
        self.moves.append(x)
        _l_(1137)
    def get_moves(self):
        _l_(1140)

        aux = self.moves
        _l_(1139)
        return aux

class Superdog(Dog):
    _l_(1145)


    #Let's try to append new fly ability to our Superdog
    def moves_setup(self):
        _l_(1144)

        #Set default moves by calling method of parent class
        super().moves_setup("hello world")
        _l_(1142)
        self.moves.append('fly')
        _l_(1143)
dog = Superdog('Freddy')
_l_(1146)
print (dog.name)
_l_(1147)
dog.moves_setup()
_l_(1148)
print (dog.get_moves()) 
_l_(1149) 

