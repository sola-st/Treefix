# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
df = DataFrame(
    {
        "A": np.array(np.random.randn(6), dtype=np.float64),
        "A1": np.array(np.random.randn(6), dtype=np.float64),
        "B": np.array(np.arange(6), dtype=np.int64),
        "C": ["foo"] * 6,
        "D": np.array([True, False] * 3, dtype=bool),
        "E": np.array(np.random.randn(6), dtype=np.float32),
        "E1": np.array(np.random.randn(6), dtype=np.float32),
        "F": np.array(np.arange(6), dtype=np.int32),
    }
)

# this is actually tricky to create the recordlike arrays and
# have the dtypes be intact
blocks = df._to_dict_of_blocks()
tuples = []
columns = []
dtypes = []
for dtype, b in blocks.items():
    columns.extend(b.columns)
    dtypes.extend([(c, np.dtype(dtype).descr[0][1]) for c in b.columns])
for i in range(len(df.index)):
    tup = []
    for _, b in blocks.items():
        tup.extend(b.iloc[i].values)
    tuples.append(tuple(tup))

recarray = np.array(tuples, dtype=dtypes).view(np.recarray)
recarray2 = df.to_records()
lists = [list(x) for x in tuples]

# tuples (lose the dtype info)
result = DataFrame.from_records(tuples, columns=columns).reindex(
    columns=df.columns
)

# created recarray and with to_records recarray (have dtype info)
result2 = DataFrame.from_records(recarray, columns=columns).reindex(
    columns=df.columns
)
result3 = DataFrame.from_records(recarray2, columns=columns).reindex(
    columns=df.columns
)

# list of tupels (no dtype info)
result4 = DataFrame.from_records(lists, columns=columns).reindex(
    columns=df.columns
)

tm.assert_frame_equal(result, df, check_dtype=False)
tm.assert_frame_equal(result2, df)
tm.assert_frame_equal(result3, df)
tm.assert_frame_equal(result4, df, check_dtype=False)

# tuples is in the order of the columns
result = DataFrame.from_records(tuples)
tm.assert_index_equal(result.columns, RangeIndex(8))

# test exclude parameter & we are casting the results here (as we don't
# have dtype info to recover)
columns_to_test = [columns.index("C"), columns.index("E1")]

exclude = list(set(range(8)) - set(columns_to_test))
result = DataFrame.from_records(tuples, exclude=exclude)
result.columns = [columns[i] for i in sorted(columns_to_test)]
tm.assert_series_equal(result["C"], df["C"])
tm.assert_series_equal(result["E1"], df["E1"])
