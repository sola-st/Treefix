# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
from l3.Runtime import _l_
try:
    import os
    _l_(644)

except ImportError:
    pass
os.path.exists("C:\\Users\\####\\Desktop\\test.txt") 
_l_(645) 
True
_l_(646)
os.path.exists("C:\\Users\\####\\Desktop\\test.tx")
_l_(647)
False
_l_(648)

