from enum import Enum # pragma: no cover

v = ['version1', 'version2'] # pragma: no cover
class TargetVersion(Enum):# pragma: no cover
    VERSION1 = 1# pragma: no cover
    VERSION2 = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compute the target versions from a --target-version flag.

    This is its own function because mypy couldn't infer the type correctly
    when it was a lambda, causing mypyc trouble.
    """
aux = [TargetVersion[val.upper()] for val in v]
_l_(15577)
exit(aux)
