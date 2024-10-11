from random import choice # pragma: no cover
import sys # pragma: no cover

class MockGrammar: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockDriver: # pragma: no cover
    def __init__(self, grammar): # pragma: no cover
        self.grammar = grammar # pragma: no cover
    def parse_string(self, src_txt, flag): # pragma: no cover
        if not src_txt or 'error' in src_txt: # pragma: no cover
            raise choice([ParseError, TokenError, IndentationError]) # pragma: no cover
 # pragma: no cover
class ParseError(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class TokenError(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class IndentationError(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
driver = type('Driver', (object,), {'Driver': MockDriver}) # pragma: no cover
grammar = MockGrammar() # pragma: no cover
src_txt = 'some source text without error' # pragma: no cover

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
