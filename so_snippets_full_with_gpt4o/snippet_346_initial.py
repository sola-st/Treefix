# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/805066/how-do-i-call-a-parent-classs-method-from-a-child-class-in-python
from l3.Runtime import _l_
class Dog(object):
    _l_(12639)

    name = ''
    _l_(12629)
    moves = []
    _l_(12630)

    def __init__(self, name):
        _l_(12632)

        self.name = name
        _l_(12631)

    def moves_setup(self,x):
        _l_(12636)

        self.moves.append('walk')
        _l_(12633)
        self.moves.append('run')
        _l_(12634)
        self.moves.append(x)
        _l_(12635)
    def get_moves(self):
        _l_(12638)

        aux = self.moves
        _l_(12637)
        return aux

class Superdog(Dog):
    _l_(12643)


    #Let's try to append new fly ability to our Superdog
    def moves_setup(self):
        _l_(12642)

        #Set default moves by calling method of parent class
        super().moves_setup("hello world")
        _l_(12640)
        self.moves.append('fly')
        _l_(12641)
dog = Superdog('Freddy')
_l_(12644)
print (dog.name)
_l_(12645)
dog.moves_setup()
_l_(12646)
print (dog.get_moves()) 
_l_(12647) 

