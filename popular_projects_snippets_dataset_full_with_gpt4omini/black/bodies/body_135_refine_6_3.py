grammar = 'some_grammar_definition' # pragma: no cover
src_txt = 'some source text' # pragma: no cover
ParseError = type('MockParseError', (Exception,), {}) # pragma: no cover
TokenError = type('MockTokenError', (Exception,), {}) # pragma: no cover

from typing import Any # pragma: no cover

class MockDriver: # pragma: no cover
    def __init__(self, grammar: Any): pass# pragma: no cover
    def parse_string(self, src: str, flag: bool): return True # pragma: no cover
driver = type('MockDriverModule', (object,), {'Driver': MockDriver})() # pragma: no cover
grammar = 'sample_grammar' # pragma: no cover
src_txt = 'sample input text' # pragma: no cover
ParseError = Exception # pragma: no cover
TokenError = Exception # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
drv = driver.Driver(grammar)
_l_(4879)
try:
    _l_(4884)

    drv.parse_string(src_txt, True)
    _l_(4880)
except (ParseError, TokenError, IndentationError):
    _l_(4882)

    aux = False
    _l_(4881)
    exit(aux)
else:
    aux = True
    _l_(4883)
    exit(aux)
