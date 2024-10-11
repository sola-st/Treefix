# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
from l3.Runtime import _l_
try:
    import sys
    _l_(14031)

except ImportError:
    pass
print("%s/%s" %(sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name))
_l_(14032)

