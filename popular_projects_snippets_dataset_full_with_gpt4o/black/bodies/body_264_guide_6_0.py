from tokenize_rt import Token # pragma: no cover

has_trailing_semicolon = False # pragma: no cover
src = 'print(\"Hello World\")' # pragma: no cover
TOKENS_TO_IGNORE = {'COMMENT', 'NL'} # pragma: no cover
class MockToken:# pragma: no cover
    def __init__(self, name, src):# pragma: no cover
        self.name = name# pragma: no cover
        self.src = src# pragma: no cover
    def _replace(self, **kwargs):# pragma: no cover
        return MockToken(self.name, kwargs.get('src', self.src)) # pragma: no cover
def src_to_tokens(src):# pragma: no cover
    return [MockToken('NAME', 'print'), MockToken('OP', '('), MockToken('STRING', '\"Hello World\"'), MockToken('OP', ')')] # pragma: no cover
def tokens_to_src(tokens):# pragma: no cover
    return ''.join(token.src for token in tokens) # pragma: no cover
def reversed_enumerate(tokens):# pragma: no cover
    return reversed(list(enumerate(tokens))) # pragma: no cover
sys.exit = print # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Put trailing semicolon back if cell originally had it.

    Mirrors the logic in `quiet` from `IPython.core.displayhook`, but uses
    ``tokenize_rt`` so that round-tripping works fine.
    """
if not has_trailing_semicolon:
    _l_(16980)

    aux = src
    _l_(16979)
    exit(aux)
try:
    from tokenize_rt import reversed_enumerate, src_to_tokens, tokens_to_src
    _l_(16982)

except ImportError:
    pass

tokens = src_to_tokens(src)
_l_(16983)
for idx, token in reversed_enumerate(tokens):
    _l_(16989)

    if token.name in TOKENS_TO_IGNORE:
        _l_(16985)

        continue
        _l_(16984)
    tokens[idx] = token._replace(src=token.src + ";")
    _l_(16986)
    break
    _l_(16987)
else:  # pragma: nocover
    raise AssertionError(
        "INTERNAL ERROR: Was not able to reinstate trailing semicolon. "
        "Please report a bug on https://github.com/psf/black/issues.  "
    ) from None
    _l_(16988)
aux = str(tokens_to_src(tokens))
_l_(16990)
exit(aux)
