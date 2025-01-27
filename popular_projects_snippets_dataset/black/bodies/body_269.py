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
    _l_(19586)

    src = src.replace(replacement.mask, replacement.src)
    _l_(19585)
aux = src
_l_(19587)
exit(aux)
