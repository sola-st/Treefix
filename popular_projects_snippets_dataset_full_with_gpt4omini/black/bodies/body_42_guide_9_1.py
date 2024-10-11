class MockLeaf:# pragma: no cover
    def __init__(self, prefix):# pragma: no cover
        self.prefix = prefix # pragma: no cover
leaf = MockLeaf('no backslash here# it should work\n\n') # pragma: no cover
inside_brackets = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Leave existing extra newlines if not `inside_brackets`. Remove everything
    else.

    Note: don't use backslashes for formatting or you'll lose your voting rights.
    """
if not inside_brackets:
    _l_(6101)

    spl = leaf.prefix.split("#")
    _l_(6094)
    if "\\" not in spl[0]:
        _l_(6100)

        nl_count = spl[-1].count("\n")
        _l_(6095)
        if len(spl) > 1:
            _l_(6097)

            nl_count -= 1
            _l_(6096)
        leaf.prefix = "\n" * nl_count
        _l_(6098)
        exit()
        _l_(6099)

leaf.prefix = ""
_l_(6102)
