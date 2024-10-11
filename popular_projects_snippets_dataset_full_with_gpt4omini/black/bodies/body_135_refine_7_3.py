src_txt = 'valid input string for parsing' # pragma: no cover
ParseError = Exception # pragma: no cover
TokenError = Exception # pragma: no cover

class MockParseError(Exception): pass # pragma: no cover
class MockTokenError(Exception): pass # pragma: no cover
class MockDriver: pass # pragma: no cover
class Mock: pass # pragma: no cover

class MockParseError(Exception): pass # pragma: no cover
class MockTokenError(Exception): pass # pragma: no cover
class MockDriver: pass # pragma: no cover
class Mock: pass # pragma: no cover
grammar = 'dummy_grammar' # pragma: no cover
src_txt = 'sample source code' # pragma: no cover
ParseError = MockParseError # pragma: no cover
TokenError = MockTokenError # pragma: no cover

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
