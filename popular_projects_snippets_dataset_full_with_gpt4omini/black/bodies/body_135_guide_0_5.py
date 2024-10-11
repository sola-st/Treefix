grammar = 'some_grammar_definition' # pragma: no cover
src_txt = 'some_source_text_with_syntax_error' # pragma: no cover
driver = type('MockDriver', (object,), {'parse_string': lambda self, txt, _ : (_ for _ in () )})() # pragma: no cover

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
