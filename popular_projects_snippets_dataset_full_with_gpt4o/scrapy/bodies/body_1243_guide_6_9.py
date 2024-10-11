import io # pragma: no cover
import csv # pragma: no cover

class MockSuperClass: # pragma: no cover
    def __init__(self, dont_fail=True, **kwargs): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
include_headers_line = True # pragma: no cover
file = io.BytesIO() # pragma: no cover
errors = 'strict' # pragma: no cover
join_multivalued = False # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self, *args, **kwargs): # pragma: no cover
        super(Mock, self).__init__(dont_fail=True, **kwargs) # pragma: no cover
        if not hasattr(self, 'encoding') or not self.encoding: # pragma: no cover
            self.encoding = 'utf-8' # pragma: no cover
        self.include_headers_line = include_headers_line # pragma: no cover
        self.stream = io.TextIOWrapper( # pragma: no cover
            file, # pragma: no cover
            line_buffering=False, # pragma: no cover
            write_through=True, # pragma: no cover
            encoding=self.encoding, # pragma: no cover
            newline='', # pragma: no cover
            errors=errors # pragma: no cover
        ) # pragma: no cover
        self.csv_writer = csv.writer(self.stream, **self._kwargs) # pragma: no cover
        self._headers_not_written = True # pragma: no cover
        self._join_multivalued = join_multivalued # pragma: no cover
 # pragma: no cover
self = type('MockClass', (MockSuperClass, Mock), {})() # pragma: no cover

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
