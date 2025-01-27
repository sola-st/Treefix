# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#24396
s1 = Series(range(1, 10))
s2 = Series("foo", index=index)

msg = "not all arguments converted during string formatting"

with pytest.raises(TypeError, match=msg):
    s2 % s1
