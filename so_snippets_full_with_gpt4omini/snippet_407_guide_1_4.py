# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
from l3.Runtime import _l_
"+7".lstrip("-+").isdigit()
_l_(3426)
True
_l_(3427)
"-7".lstrip("-+").isdigit()
_l_(3428)
True
_l_(3429)
"7".lstrip("-+").isdigit()
_l_(3430)
True
_l_(3431)
"13.4".lstrip("-+").isdigit()
_l_(3432)
False
_l_(3433)

def is_int(val):
   _l_(3435)

   aux = val.lstrip("-+").isdigit()
   _l_(3434)
   return aux

