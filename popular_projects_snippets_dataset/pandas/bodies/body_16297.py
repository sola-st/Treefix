# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#41734 disallow silent overflow, enforced in 2.0
msg = "Values are too large to be losslessly converted"
with pytest.raises(ValueError, match=msg):
    Series([1, 200, 923442], dtype="int8")

with pytest.raises(ValueError, match=msg):
    Series([1, 200, 923442], dtype="uint8")
