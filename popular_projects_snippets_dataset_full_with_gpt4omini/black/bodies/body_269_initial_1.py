class Replacement:# pragma: no cover
    def __init__(self, mask, src):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src# pragma: no cover
# pragma: no cover
replacements = [Replacement("9b20", "foo")] # pragma: no cover
src = "9b20\nfoo = bar" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Remove replacements from cell.

    For example

        "9b20"
        foo = bar

    becomes

        %%time
        foo = bar
    """
for replacement in replacements:
    _l_(8171)

    src = src.replace(replacement.mask, replacement.src)
    _l_(8170)
aux = src
_l_(8172)
exit(aux)
