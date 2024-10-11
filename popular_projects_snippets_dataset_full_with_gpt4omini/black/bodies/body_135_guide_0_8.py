grammar = 'grammar_definition_here' # pragma: no cover
src_txt = 'some source text that will not raise an error' # pragma: no cover
driver = type('MockDriver', (object,), {'parse_string': lambda self, txt, flag: None}) # pragma: no cover
driver.Driver = type('Mock', (object,), {'__init__': lambda self, g: None, 'parse_string': lambda self, txt, flag: None}) # pragma: no cover

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
