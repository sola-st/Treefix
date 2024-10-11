inside_brackets = False # pragma: no cover
leaf = type('Mock', (object,), {'prefix': 'sample text #\n'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Leave existing extra newlines if not `inside_brackets`. Remove everything
    else.

    Note: don't use backslashes for formatting or you'll lose your voting rights.
    """
if not inside_brackets:
    _l_(17612)

    spl = leaf.prefix.split("#")
    _l_(17605)
    if "\\" not in spl[0]:
        _l_(17611)

        nl_count = spl[-1].count("\n")
        _l_(17606)
        if len(spl) > 1:
            _l_(17608)

            nl_count -= 1
            _l_(17607)
        leaf.prefix = "\n" * nl_count
        _l_(17609)
        exit()
        _l_(17610)

leaf.prefix = ""
_l_(17613)
