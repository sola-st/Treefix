# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6886493/get-all-object-attributes-in-python
from l3.Runtime import _l_
class MyObj(object):
  _l_(13492)

  def __init__(self):
    _l_(13491)

    self.name = 'Chuck Norris'
    _l_(13489)
    self.phone = '+6661'
    _l_(13490)

obj = MyObj()
_l_(13493)
print(obj.__dict__)
_l_(13494)
print(dir(obj))
_l_(13495)

# Output:  
# obj.__dict__ --> {'phone': '+6661', 'name': 'Chuck Norris'}
#
# dir(obj)     --> ['__class__', '__delattr__', '__dict__', '__doc__',
#               '__format__', '__getattribute__', '__hash__', 
#               '__init__', '__module__', '__new__', '__reduce__', 
#               '__reduce_ex__', '__repr__', '__setattr__', 
#               '__sizeof__', '__str__', '__subclasshook__', 
#               '__weakref__', 'name', 'phone']

