import difflib # pragma: no cover

def assert_equivalent(src, dst):# pragma: no cover
    if src != dst:# pragma: no cover
        raise AssertionError('Source and destination contents are not equivalent') # pragma: no cover
src_contents = 'This is a test content for source.' # pragma: no cover
dst_contents = 'This is a test content for source.' # pragma: no cover
def assert_stable(src, dst, mode):# pragma: no cover
    if mode == 'check' and difflib.SequenceMatcher(None, src, dst).ratio() != 1.0:# pragma: no cover
        raise AssertionError('Content is not stable on second pass')# pragma: no cover
    elif mode == 'modify':# pragma: no cover
        dst_modified = dst + ' modified'# pragma: no cover
        if difflib.SequenceMatcher(None, src, dst_modified).ratio() == 1.0:# pragma: no cover
            raise AssertionError('Content is not stable after modification') # pragma: no cover
mode = 'check' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Perform stability and equivalence checks.

    Raise AssertionError if source and destination contents are not
    equivalent, or if a second pass of the formatter would format the
    content differently.
    """
assert_equivalent(src_contents, dst_contents)
_l_(16405)
assert_stable(src_contents, dst_contents, mode=mode)
_l_(16406)
