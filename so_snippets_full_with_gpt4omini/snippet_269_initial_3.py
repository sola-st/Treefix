# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/730764/how-to-properly-ignore-exceptions
from l3.Runtime import _l_
try:
    _l_(2171)

    doSomething()
    _l_(2168)
except:
    _l_(2170)

    _ = ""
    _l_(2169)

