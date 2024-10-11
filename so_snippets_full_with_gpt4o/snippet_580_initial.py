# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16720541/python-string-replace-regular-expression
from l3.Runtime import _l_
try:
    import re
    _l_(14026)

except ImportError:
    pass
s = "Example String"
_l_(14027)
replaced = re.sub('[ES]', 'a', s)
_l_(14028)
print(replaced)
_l_(14029)

