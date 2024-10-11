# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
ymd = multiindex_year_month_day_dataframe_random_data
s = ymd["A"]

s[2000, 3] = np.nan
assert isna(s.values[42:65]).all()
assert notna(s.values[:42]).all()
assert notna(s.values[65:]).all()

s[2000, 3, 10] = np.nan
assert isna(s.iloc[49])

with pytest.raises(KeyError, match="49"):
    # GH#33355 dont fall-back to positional when leading level is int
    s[49]
