# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
from l3.Runtime import _l_
try:
    import getpass
    _l_(319)

except ImportError:
    pass
getpass.getuser()
_l_(320)
'kostya'
_l_(321)

