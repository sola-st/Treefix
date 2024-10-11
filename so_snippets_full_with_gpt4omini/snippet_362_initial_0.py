import re # pragma: no cover

string_to_split = 'Beautiful, is; better*than\nugly' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
from l3.Runtime import _l_
try:
    import re
    _l_(387)

except ImportError:
    pass
re.split('; |, ', string_to_split)
_l_(388)

a='Beautiful, is; better*than\nugly'
_l_(389)
try:
    import re
    _l_(391)

except ImportError:
    pass
re.split('; |, |\*|\n',a)
_l_(392)
['Beautiful', 'is', 'better', 'than', 'ugly']
_l_(393)

