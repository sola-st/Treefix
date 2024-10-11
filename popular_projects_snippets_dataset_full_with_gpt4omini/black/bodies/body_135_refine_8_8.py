grammar = 'your_grammar_here' # pragma: no cover
src_txt = 'your_source_text_here' # pragma: no cover

from types import SimpleNamespace # pragma: no cover

driver = SimpleNamespace() # pragma: no cover
driver.Driver = type('Driver', (object,), {'__init__': lambda self, grammar: None, 'parse_string': lambda self, txt, flag: None}) # pragma: no cover
grammar = 'example_grammar_definition' # pragma: no cover
src_txt = 'example input string' # pragma: no cover
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
