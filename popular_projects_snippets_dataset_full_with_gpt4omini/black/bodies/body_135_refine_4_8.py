grammar = 'some_grammar_definition' # pragma: no cover
src_txt = 'some_input_string' # pragma: no cover
ParseError = type('ParseError', (Exception,), {}) # pragma: no cover
TokenError = type('TokenError', (Exception,), {}) # pragma: no cover

from typing import Any # pragma: no cover

grammar = 'mock_grammar_definition' # pragma: no cover
src_txt = 'mock source text' # pragma: no cover
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
