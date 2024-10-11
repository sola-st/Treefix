# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series([1, 2])
with pytest.raises(ValueError, match="invalid_kind is not a valid plot kind"):
    s.plot(kind="invalid_kind")
