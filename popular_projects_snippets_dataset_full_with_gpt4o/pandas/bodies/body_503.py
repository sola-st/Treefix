# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
with pytest.raises(ValueError, match="closed must be one of"):
    IntervalDtype(np.float64, "foo")
