# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
a = Series(["a", "b", "c"])
b = Series(["b", "a"])
msg = "only compare identically-labeled Series"
with pytest.raises(ValueError, match=msg):
    a < b

a = Series([1, 2])
b = Series([2, 3, 4])
with pytest.raises(ValueError, match=msg):
    a == b
