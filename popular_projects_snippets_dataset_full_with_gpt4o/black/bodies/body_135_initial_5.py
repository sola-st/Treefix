driver = type('MockDriver', (object,), {'Driver': type('DriverClass', (object,), {'parse_string': lambda self, x, y: None})})() # pragma: no cover
grammar = 'mock_grammar_definition' # pragma: no cover
src_txt = 'some sample source text' # pragma: no cover
ParseError = type('ParseError', (Exception,), {}) # pragma: no cover
TokenError = type('TokenError', (Exception,), {}) # pragma: no cover

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
