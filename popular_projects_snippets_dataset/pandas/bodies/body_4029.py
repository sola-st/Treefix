# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# GH#2179

data = {1: ["foo"], 2: ["bar"]}

result = DataFrame.from_records(data, columns=["a", "b"])
exp = DataFrame(data, columns=["a", "b"])
tm.assert_frame_equal(result, exp)

# overlap in index/index_names

data = {"a": [1, 2, 3], "b": [4, 5, 6]}

result = DataFrame.from_records(data, index=["a", "b", "c"])
exp = DataFrame(data, index=["a", "b", "c"])
tm.assert_frame_equal(result, exp)

# GH#2623
rows = []
rows.append([datetime(2010, 1, 1), 1])
rows.append([datetime(2010, 1, 2), "hi"])  # test col upconverts to obj
df2_obj = DataFrame.from_records(rows, columns=["date", "test"])
result = df2_obj.dtypes
expected = Series(
    [np.dtype("datetime64[ns]"), np.dtype("object")], index=["date", "test"]
)
tm.assert_series_equal(result, expected)

rows = []
rows.append([datetime(2010, 1, 1), 1])
rows.append([datetime(2010, 1, 2), 1])
df2_obj = DataFrame.from_records(rows, columns=["date", "test"])
result = df2_obj.dtypes
expected = Series(
    [np.dtype("datetime64[ns]"), np.dtype("int64")], index=["date", "test"]
)
tm.assert_series_equal(result, expected)
