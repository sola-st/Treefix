yourObject = None # pragma: no cover
yourString = "" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3289601/null-object-in-python
from l3.Runtime import _l_
if yourObject is None:
    _l_(12520)

    ...
    _l_(12519)

if yourString == "":
    _l_(12522)

    ...
    _l_(12521)

