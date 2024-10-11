from collections import namedtuple # pragma: no cover

driver = type('Mock', (object,), {'Driver': lambda grammar: type('MockDriver', (object,), {'parse_string': lambda self, src_txt, flag: None})()})() # pragma: no cover
grammar = 'mock_grammar' # pragma: no cover
src_txt = 'mock_source_text' # pragma: no cover
ParseError = namedtuple('ParseError', '') # pragma: no cover
TokenError = namedtuple('TokenError', '') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
drv = driver.Driver(grammar)
_l_(16673)
try:
    _l_(16678)

    drv.parse_string(src_txt, True)
    _l_(16674)
except (ParseError, TokenError, IndentationError):
    _l_(16676)

    aux = False
    _l_(16675)
    exit(aux)
else:
    aux = True
    _l_(16677)
    exit(aux)
