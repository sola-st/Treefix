# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/699866/python-int-to-binary-string
from l3.Runtime import _l_
def dectobin(number):
    _l_(452)

    bin = ''
    _l_(447)
    while (number >= 1):
        _l_(450)

        number, rem = divmod(number, 2)
        _l_(448)
        bin = bin + str(rem)
        _l_(449)
    aux = bin
    _l_(451)
    return aux

