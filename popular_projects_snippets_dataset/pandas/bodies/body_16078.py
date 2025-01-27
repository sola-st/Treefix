# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
invalid = Series([1, 2, 3]).astype("category")
msg = "Can only use .dt accessor with datetimelike"

with pytest.raises(AttributeError, match=msg):
    invalid.dt
assert not hasattr(invalid, "str")
