import io # pragma: no cover
import os # pragma: no cover

sys = type('Mock', (object,), {'stdout': io.StringIO(), 'stderr': io.StringIO(), 'stdin': io.StringIO()})() # pragma: no cover
open = lambda filename, mode, buffering: io.StringIO() # pragma: no cover

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

