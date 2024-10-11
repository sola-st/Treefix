grammar = 'example grammar' # pragma: no cover
src_txt = 'example source text' # pragma: no cover
class MockDriver: # pragma: no cover
    def __init__(self, grammar): # pragma: no cover
        self.grammar = grammar # pragma: no cover
    def parse_string(self, src_txt, flag): # pragma: no cover
        pass # pragma: no cover

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
