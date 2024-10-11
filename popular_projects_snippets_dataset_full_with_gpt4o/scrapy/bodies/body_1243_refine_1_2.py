import io # pragma: no cover
import csv # pragma: no cover

kwargs = {} # pragma: no cover
self = type('Mock', (object,), {'encoding': None, '_kwargs': {}, 'include_headers_line': None, 'stream': None, 'csv_writer': None, '_headers_not_written': None, '_join_multivalued': None})() # pragma: no cover
include_headers_line = True # pragma: no cover
file = open('dummy_file.csv', 'w+') # pragma: no cover
errors = 'strict' # pragma: no cover
join_multivalued = False # pragma: no cover

import io # pragma: no cover
import csv # pragma: no cover

kwargs = {} # pragma: no cover
class BaseClass: pass # pragma: no cover
# Assume BaseClass is the superclass required by the original code # pragma: no cover
class MockSelf(BaseClass): # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super().__init__(*args, **kwargs) # pragma: no cover
        self.encoding = None # pragma: no cover
        self._kwargs = {} # pragma: no cover
        self.include_headers_line = None # pragma: no cover
        self.stream = None # pragma: no cover
        self.csv_writer = None # pragma: no cover
        self._headers_not_written = None # pragma: no cover
        self._join_multivalued = None # pragma: no cover
self = MockSelf() # pragma: no cover
include_headers_line = True # pragma: no cover
file = open('dummy_file.csv', 'w+') # pragma: no cover
errors = 'strict' # pragma: no cover
join_multivalued = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
super().__init__(dont_fail=True, **kwargs)
_l_(20819)
if not self.encoding:
    _l_(20821)

    self.encoding = 'utf-8'
    _l_(20820)
self.include_headers_line = include_headers_line
_l_(20822)
self.stream = io.TextIOWrapper(
    file,
    line_buffering=False,
    write_through=True,
    encoding=self.encoding,
    newline='',  # Windows needs this https://github.com/scrapy/scrapy/issues/3034
    errors=errors,
)
_l_(20823)
self.csv_writer = csv.writer(self.stream, **self._kwargs)
_l_(20824)
self._headers_not_written = True
_l_(20825)
self._join_multivalued = join_multivalued
_l_(20826)
