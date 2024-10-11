# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/107705/disable-output-buffering
from l3.Runtime import _l_
try:
    import sys
    _l_(15142)

except ImportError:
    pass
myFile= open( "a.log", "w", 0 ) 
_l_(15143) 
sys.stdout= myFile
_l_(15144)

