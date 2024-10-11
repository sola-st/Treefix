# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/730764/how-to-properly-ignore-exceptions
from l3.Runtime import _l_
try:
    _l_(13499)

    doSomething()
    _l_(13496)
except:
    _l_(13498)

    _ = ""
    _l_(13497)

