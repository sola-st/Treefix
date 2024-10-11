# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/733454/best-way-to-format-integer-as-string-with-leading-zeros
from l3.Runtime import _l_
add_nulls = lambda number, zero_count : "{0:0{1}d}".format(number, zero_count)
_l_(2089)

add_nulls(2,3)
_l_(2090)
'002'
_l_(2091)

