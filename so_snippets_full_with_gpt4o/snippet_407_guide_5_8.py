# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
from l3.Runtime import _l_
"+7".lstrip("-+").isdigit()
_l_(13784)
True
_l_(13785)
"-7".lstrip("-+").isdigit()
_l_(13786)
True
_l_(13787)
"7".lstrip("-+").isdigit()
_l_(13788)
True
_l_(13789)
"13.4".lstrip("-+").isdigit()
_l_(13790)
False
_l_(13791)

def is_int(val):
   _l_(13793)

   aux = val.lstrip("-+").isdigit()
   _l_(13792)
   return aux

