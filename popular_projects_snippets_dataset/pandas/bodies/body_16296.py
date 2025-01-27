# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
msg = "could not convert string to float"
with pytest.raises(ValueError, match=msg):
    Series(["a", "b", "c"], dtype=float)
