# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# https://github.com/pandas-dev/pandas/pull/42950 - when selecting a column
# from dataframe, don't try to infer object dtype index on Series construction
idx = date_range("2012", periods=3).astype(object)
df = DataFrame({0: [1, 2, 3]}, index=idx)
assert df.index.dtype == object

if indexer is tm.getitem:
    ser = indexer(df)[0]
else:
    ser = indexer(df)[:, 0]

assert ser.index.dtype == object
