src_txt = 'some input that causes a parse error' # pragma: no cover
grammar = type('MockGrammar', (object,), {})() # pragma: no cover
driver = type('MockDriver', (object,), {'Driver': type('Mock', (object,), {'parse_string': lambda self, txt, flag: (_ for _ in ()).throw(ParseError())})()}) # pragma: no cover

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
