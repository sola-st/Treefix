# Extracted from ./data/repos/pandas/pandas/tests/base/test_fillna.py
# GH 11343
obj = index_or_series_obj

if isinstance(obj, MultiIndex):
    msg = "isna is not defined for MultiIndex"
    with pytest.raises(NotImplementedError, match=msg):
        obj.fillna(0)
    exit()

# values will not be changed
fill_value = obj.values[0] if len(obj) > 0 else 0
result = obj.fillna(fill_value)

tm.assert_equal(obj, result)

# check shallow_copied
assert obj is not result
