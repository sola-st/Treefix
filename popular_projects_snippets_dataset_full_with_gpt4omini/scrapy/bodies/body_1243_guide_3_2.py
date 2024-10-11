import io # pragma: no cover
import csv # pragma: no cover

class MockBase: pass # pragma: no cover
class MockClass(MockBase): # pragma: no cover
    def __init__(self, include_headers_line=True, join_multivalued=False, errors='strict', **kwargs): # pragma: no cover
        self.encoding = None # pragma: no cover
        self.include_headers_line = include_headers_line # pragma: no cover
        self._kwargs = kwargs # pragma: no cover
        file = io.StringIO() # pragma: no cover
        if not self.encoding: self.encoding = 'utf-8' # pragma: no cover
        self.stream = io.TextIOWrapper(file, line_buffering=False, write_through=True, encoding=self.encoding, newline='', errors=errors) # pragma: no cover
        self.csv_writer = csv.writer(self.stream, **self._kwargs) # pragma: no cover
        self._headers_not_written = True # pragma: no cover
        self._join_multivalued = join_multivalued # pragma: no cover
self = MockClass() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/exporters.py
from l3.Runtime import _l_
super().__init__(dont_fail=True, **kwargs)
_l_(9690)
if not self.encoding:
    _l_(9692)

    self.encoding = 'utf-8'
    _l_(9691)
self.include_headers_line = include_headers_line
_l_(9693)
self.stream = io.TextIOWrapper(
    file,
    line_buffering=False,
    write_through=True,
    encoding=self.encoding,
    newline='',  # Windows needs this https://github.com/scrapy/scrapy/issues/3034
    errors=errors,
)
_l_(9694)
self.csv_writer = csv.writer(self.stream, **self._kwargs)
_l_(9695)
self._headers_not_written = True
_l_(9696)
self._join_multivalued = join_multivalued
_l_(9697)
