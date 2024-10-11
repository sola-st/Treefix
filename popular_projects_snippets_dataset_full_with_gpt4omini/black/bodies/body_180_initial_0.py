from typing import Dict # pragma: no cover

v = ['1.0', '2.0', '3.0'] # pragma: no cover
TargetVersion = {'1.0': 'Version One', '2.0': 'Version Two', '3.0': 'Version Three'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compute the target versions from a --target-version flag.

    This is its own function because mypy couldn't infer the type correctly
    when it was a lambda, causing mypyc trouble.
    """
aux = [TargetVersion[val.upper()] for val in v]
_l_(3821)
exit(aux)
