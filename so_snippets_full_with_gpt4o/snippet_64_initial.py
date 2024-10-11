# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
from l3.Runtime import _l_
value = 5.34343
_l_(12764)
rounded_value = round(value, 2) # 5.34
_l_(12765) # 5.34

