# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/699866/python-int-to-binary-string
from l3.Runtime import _l_
def dectobin(number):
    _l_(12588)

    bin = ''
    _l_(12583)
    while (number >= 1):
        _l_(12586)

        number, rem = divmod(number, 2)
        _l_(12584)
        bin = bin + str(rem)
        _l_(12585)
    aux = bin
    _l_(12587)
    return aux

