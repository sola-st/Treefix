import re # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
from l3.Runtime import _l_
re.search('test', ' test')      # returns a Truthy match object (because the search starts from any index) 
_l_(2575)      # returns a Truthy match object (because the search starts from any index) 

re.match('test', ' test')       # returns None (because the search start from 0 index)
_l_(2576)       # returns None (because the search start from 0 index)
re.match('test', 'test')        # returns a Truthy match object (match at 0 index)
_l_(2577)        # returns a Truthy match object (match at 0 index)

