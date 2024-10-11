# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it
from l3.Runtime import _l_
obj.a = type('Test', (object,), {})  
_l_(13324)  
obj.a.b = 'fun'  
_l_(13325)  

obj.b = lambda:None
_l_(13326)

class Test:
  _l_(13328)

  pass
  _l_(13327)
obj.c = Test()
_l_(13329)

