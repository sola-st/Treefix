# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH#18185
ser = Series([1, 2, 3, 1], dtype="category")
msg = r"Cannot setitem on a Categorical with a new category \(-1\)"
with pytest.raises(TypeError, match=msg):
    ser.reindex([1, 2, 3, 4, 5], fill_value=-1)
