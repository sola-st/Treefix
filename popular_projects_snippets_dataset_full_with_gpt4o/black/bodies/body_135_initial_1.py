from types import SimpleNamespace # pragma: no cover

grammar = 'start: "a"' # pragma: no cover
driver = SimpleNamespace(Driver=type('Driver', (object,), {'__init__': lambda self, grammar: None, 'parse_string': lambda self, text, start: None})) # pragma: no cover
src_txt = 'a' # pragma: no cover

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
