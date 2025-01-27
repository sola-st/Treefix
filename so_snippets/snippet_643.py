# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1489599/how-do-i-find-out-my-pythonpath-using-python
from l3.Runtime import _l_
try:
    import sys
    _l_(443)

except ImportError:
    pass
for a in sys.path:
    _l_(446)

    a = a.replace('\\\\','\\')
    _l_(444)
    print(a)
    _l_(445)

