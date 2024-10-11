import os # pragma: no cover
import types # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(11956)

except ImportError:
    pass

if not os.environ.get("DEBUSSY"):
    _l_(11959)

    os.environ.setdefault("DEBUSSY","1")
    _l_(11957)
else:
     os.environ["DEBUSSY"] = "1"
     _l_(11958)

print(os.environ["DEBUSSY"])
_l_(11960)


