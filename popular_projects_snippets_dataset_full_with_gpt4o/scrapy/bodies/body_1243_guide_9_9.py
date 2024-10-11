import io # pragma: no cover
import csv # pragma: no cover

file = io.BytesIO() # pragma: no cover
kwargs = {} # pragma: no cover
include_headers_line = True # pragma: no cover
errors = 'strict' # pragma: no cover
join_multivalued = False # pragma: no cover
class MockSuper: # pragma: no cover
    def __init__(self, dont_fail=True, **kwargs): # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (MockSuper,), { # pragma: no cover
    'encoding': None, # pragma: no cover
    '_kwargs': kwargs # pragma: no cover
})() # pragma: no cover

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
