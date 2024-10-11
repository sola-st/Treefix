from tokenize_rt import Token # pragma: no cover

src = 'fig, ax = plt.subplots()\nax.plot(x_data, y_data);  # plot data' # pragma: no cover
TOKENS_TO_IGNORE = {'NEWLINE', 'COMMENT', 'NL'} # pragma: no cover

from tokenize_rt import src_to_tokens, tokens_to_src, reversed_enumerate, Token # pragma: no cover

src = 'fig, ax = plt.subplots()\nax.plot(x_data, y_data);  # plot data\n' # pragma: no cover
TOKENS_TO_IGNORE = {'COMMENT', 'NL', 'NEWLINE', 'INDENT', 'DEDENT'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Remove trailing semicolon from Jupyter notebook cell.

    For example,

        fig, ax = plt.subplots()
        ax.plot(x_data, y_data);  # plot data

    would become

        fig, ax = plt.subplots()
        ax.plot(x_data, y_data)  # plot data

    Mirrors the logic in `quiet` from `IPython.core.displayhook`, but uses
    ``tokenize_rt`` so that round-tripping works fine.
    """
try:
    from tokenize_rt import reversed_enumerate, src_to_tokens, tokens_to_src
    _l_(16564)

except ImportError:
    pass

tokens = src_to_tokens(src)
_l_(16565)
trailing_semicolon = False
_l_(16566)
for idx, token in reversed_enumerate(tokens):
    _l_(16573)

    if token.name in TOKENS_TO_IGNORE:
        _l_(16568)

        continue
        _l_(16567)
    if token.name == "OP" and token.src == ";":
        _l_(16571)

        del tokens[idx]
        _l_(16569)
        trailing_semicolon = True
        _l_(16570)
    break
    _l_(16572)
if not trailing_semicolon:
    _l_(16575)

    aux = (src, False)
    _l_(16574)
    exit(aux)
aux = (tokens_to_src(tokens), True)
_l_(16576)
exit(aux)
