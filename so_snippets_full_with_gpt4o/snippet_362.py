# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
from l3.Runtime import _l_
try:
    import re
    _l_(12285)

except ImportError:
    pass
re.split('; |, ', string_to_split)
_l_(12286)

a='Beautiful, is; better*than\nugly'
_l_(12287)
try:
    import re
    _l_(12289)

except ImportError:
    pass
re.split('; |, |\*|\n',a)
_l_(12290)
['Beautiful', 'is', 'better', 'than', 'ugly']
_l_(12291)

