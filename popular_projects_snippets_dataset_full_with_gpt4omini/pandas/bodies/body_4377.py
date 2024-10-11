# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
rec = float_frame.to_records(index=False)
rec.dtype.names = list(rec.dtype.names)[::-1]

index = float_frame.index

df = DataFrame(rec)
tm.assert_index_equal(df.columns, Index(rec.dtype.names))

df2 = DataFrame(rec, index=index)
tm.assert_index_equal(df2.columns, Index(rec.dtype.names))
tm.assert_index_equal(df2.index, index)

# case with columns != the ones we would infer from the data
rng = np.arange(len(rec))[::-1]
df3 = DataFrame(rec, index=rng, columns=["C", "B"])
expected = DataFrame(rec, index=rng).reindex(columns=["C", "B"])
tm.assert_frame_equal(df3, expected)
