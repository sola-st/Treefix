# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24617397/how-to-print-to-console-in-pytest
from l3.Runtime import _l_
try:
    import warnings
    _l_(13321)

except ImportError:
    pass

text = "asdf" 
_l_(13322) 

warnings.warn(UserWarning("{}".format(text)))
_l_(13323)

