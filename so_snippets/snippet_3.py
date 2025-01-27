# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
from l3.Runtime import _l_
if conditionX:
    _l_(630)

    print('yes')
    _l_(628)
else:
    print('nah')
    _l_(629)

print('yes') if conditionX else print('nah')
_l_(631)

