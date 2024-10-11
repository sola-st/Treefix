from typing import Callable # pragma: no cover

def assert_equivalent(a, b): assert a == b, 'Contents do not match' # pragma: no cover
src_contents = 'Sample source content for testing.' # pragma: no cover
dst_contents = 'Sample source content for testing.' # pragma: no cover
def assert_stable(a, b, mode): assert a == b, 'Contents are not stable' # pragma: no cover
mode = 'strict' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Perform stability and equivalence checks.

    Raise AssertionError if source and destination contents are not
    equivalent, or if a second pass of the formatter would format the
    content differently.
    """
assert_equivalent(src_contents, dst_contents)
_l_(4595)
assert_stable(src_contents, dst_contents, mode=mode)
_l_(4596)
