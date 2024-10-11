obj = type('Mock', (object,), {})() # pragma: no cover
obj.a = type('Test', (object,), {})() # pragma: no cover
obj.a.b = 'fun' # pragma: no cover
obj.b = lambda: None # pragma: no cover
class Test: pass # pragma: no cover
obj.c = Test() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it
from l3.Runtime import _l_
obj.a = type('Test', (object,), {})  
_l_(1275)  
obj.a.b = 'fun'  
_l_(1276)  

obj.b = lambda:None
_l_(1277)

class Test:
  _l_(1279)

  pass
  _l_(1278)
obj.c = Test()
_l_(1280)

