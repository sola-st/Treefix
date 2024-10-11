# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_generic.py
# GH 38588, 46719
if abctype1 == abctype2:
    assert issubclass(type(inst), getattr(gt, abctype2))

    with pytest.raises(
        TypeError, match=re.escape("issubclass() arg 1 must be a class")
    ):
        issubclass(inst, getattr(gt, abctype2))
else:
    assert not issubclass(type(inst), getattr(gt, abctype2))
