from tokenize_rt import Token # pragma: no cover

has_trailing_semicolon = False # pragma: no cover
src = 'print("Hello, world!")' # pragma: no cover
TOKENS_TO_IGNORE = {'COMMENT', 'NL', 'NEWLINE', 'WHITESPACE'} # pragma: no cover

from tokenize_rt import Token # pragma: no cover

has_trailing_semicolon = False # pragma: no cover
src = 'print(\"Hello, World!\")' # pragma: no cover
TOKENS_TO_IGNORE = {'COMMENT', 'NL', 'STRING', 'NAME', 'OP', 'ENDMARKER'} # pragma: no cover

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
