# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_generic.py
# GH 38588, 46719
if abctype1 == abctype2:
    assert isinstance(inst, getattr(gt, abctype2))
    assert not isinstance(type(inst), getattr(gt, abctype2))
else:
    assert not isinstance(inst, getattr(gt, abctype2))
