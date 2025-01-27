# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile
from l3.Runtime import _l_
re.search('test', 'TeSt', re.IGNORECASE)
_l_(329)
re.match('test', 'TeSt', re.IGNORECASE)
_l_(330)
re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE)
_l_(331)

