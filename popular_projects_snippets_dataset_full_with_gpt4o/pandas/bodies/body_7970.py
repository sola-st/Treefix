# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
with pytest.raises(AssertionError, match="<class "):
    PeriodIndex._simple_new(floats)

msg = "PeriodIndex does not allow floating point in construction"
with pytest.raises(TypeError, match=msg):
    PeriodIndex(floats)
