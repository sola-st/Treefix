# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
ymd = multiindex_year_month_day_dataframe_random_data

result = ymd.loc[2000]
result2 = ymd["A"].loc[2000]
assert result.index.names == ymd.index.names[1:]
assert result2.index.names == ymd.index.names[1:]

result = ymd.loc[2000, 2]
result2 = ymd["A"].loc[2000, 2]
assert result.index.name == ymd.index.names[2]
assert result2.index.name == ymd.index.names[2]
