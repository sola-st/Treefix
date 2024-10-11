# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
ymd = multiindex_year_month_day_dataframe_random_data

new_index = ymd.index[::10]
chunk = ymd.reindex(new_index)
assert chunk.index is new_index

chunk = ymd.loc[new_index]
assert chunk.index.equals(new_index)

ymdT = ymd.T
chunk = ymdT.reindex(columns=new_index)
assert chunk.columns is new_index

chunk = ymdT.loc[:, new_index]
assert chunk.columns.equals(new_index)
