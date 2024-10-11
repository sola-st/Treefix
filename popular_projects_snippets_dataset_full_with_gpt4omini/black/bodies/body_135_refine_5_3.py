grammar = 'example_grammar' # pragma: no cover
src_txt = 'example source text' # pragma: no cover

class ParseError(Exception): pass # pragma: no cover
class TokenError(Exception): pass # pragma: no cover

class ParseError(Exception): pass # pragma: no cover
class TokenError(Exception): pass # pragma: no cover

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
