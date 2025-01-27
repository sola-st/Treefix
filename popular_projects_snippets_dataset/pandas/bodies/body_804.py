# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_generic.py
# GH 38588
if abctype in subs:
    assert isinstance(inst, getattr(gt, parent))
else:
    assert not isinstance(inst, getattr(gt, parent))
