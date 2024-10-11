# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_partial.py
# GH#33355 dont fall-back to positional when leading level is int
ymd = multiindex_year_month_day_dataframe_random_data
levels = ymd.index.levels
ymd.index = ymd.index.set_levels([levels[0].astype(dtype)] + levels[1:])
ser = ymd["A"]
mi = ser.index
assert isinstance(mi, MultiIndex)
if dtype is int:
    assert mi.levels[0].dtype == np.int_
else:
    assert mi.levels[0].dtype == np.float64

assert 14 not in mi.levels[0]
assert not mi.levels[0]._should_fallback_to_positional
assert not mi._should_fallback_to_positional

with pytest.raises(KeyError, match="14"):
    ser[14]
