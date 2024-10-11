grammar = 'some_grammar_definition' # pragma: no cover
src_txt = 'sample text for parsing' # pragma: no cover

class MockParseError(Exception): pass # pragma: no cover
class MockTokenError(Exception): pass # pragma: no cover
class MockDriver:# pragma: no cover
    def __init__(self, grammar):# pragma: no cover
        self.grammar = grammar# pragma: no cover
    def parse_string(self, src_txt, flag):# pragma: no cover
        return True # pragma: no cover
driver = type('driver', (), {'Driver': MockDriver})() # pragma: no cover
grammar = 'some_grammar_definition' # pragma: no cover
src_txt = 'sample input text' # pragma: no cover
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
