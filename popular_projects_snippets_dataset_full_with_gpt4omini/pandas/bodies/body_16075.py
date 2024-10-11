# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# https://github.com/pandas-dev/pandas/issues/10673
cat = Series(list("aabbcde")).astype("category")
with pytest.raises(AttributeError, match="You cannot add any new attribute"):
    cat.cat.xlabel = "a"
