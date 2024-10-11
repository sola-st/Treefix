from tokenize_rt import reversed_enumerate, src_to_tokens, tokens_to_src # pragma: no cover

src = 'fig, ax = plt.subplots()\nax.plot(x_data, y_data);  # plot data\n' # pragma: no cover
TOKENS_TO_IGNORE = ['NEWLINE', 'NL', 'COMMENT'] # pragma: no cover

from tokenize_rt import reversed_enumerate, src_to_tokens, tokens_to_src # pragma: no cover

TOKENS_TO_IGNORE = ['NEWLINE', 'NL', 'COMMENT'] # pragma: no cover

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
    _l_(4724)

except ImportError:
    pass

tokens = src_to_tokens(src)
_l_(4725)
trailing_semicolon = False
_l_(4726)
for idx, token in reversed_enumerate(tokens):
    _l_(4733)

    if token.name in TOKENS_TO_IGNORE:
        _l_(4728)

        continue
        _l_(4727)
    if token.name == "OP" and token.src == ";":
        _l_(4731)

        del tokens[idx]
        _l_(4729)
        trailing_semicolon = True
        _l_(4730)
    break
    _l_(4732)
if not trailing_semicolon:
    _l_(4735)

    aux = (src, False)
    _l_(4734)
    exit(aux)
aux = (tokens_to_src(tokens), True)
_l_(4736)
exit(aux)
