# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# GH#9322

assert Series.cat is CategoricalAccessor
ser = Series(list("aabbcde")).astype("category")
assert isinstance(ser.cat, CategoricalAccessor)

invalid = Series([1])
with pytest.raises(AttributeError, match="only use .cat accessor"):
    invalid.cat
assert not hasattr(invalid, "cat")
