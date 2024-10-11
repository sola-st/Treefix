# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
from l3.Runtime import _l_
try:
    import os
    _l_(12311)

except ImportError:
    pass
os.path.exists("C:\\Users\\####\\Desktop\\test.txt") 
_l_(12312) 
True
_l_(12313)
os.path.exists("C:\\Users\\####\\Desktop\\test.tx")
_l_(12314)
False
_l_(12315)

