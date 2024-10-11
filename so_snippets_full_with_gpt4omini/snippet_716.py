# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/25445439/what-does-syntaxerror-missing-parentheses-in-call-to-print-mean-in-python
from l3.Runtime import _l_
items = ['foo', 'bar', 'baz']
_l_(3411)
print(*items, sep='+')
_l_(3412)
foo+bar+baz
_l_(3413)

