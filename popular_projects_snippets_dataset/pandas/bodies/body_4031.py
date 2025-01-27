# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
a = np.array([(1, 2)], dtype=[("id", np.int64), ("value", np.int64)])
df = DataFrame.from_records(a, index="id")

ex_index = Index([1], name="id")
expected = DataFrame({"value": [2]}, index=ex_index, columns=["value"])
tm.assert_frame_equal(df, expected)

b = a[:0]
df2 = DataFrame.from_records(b, index="id")
tm.assert_frame_equal(df2, df.iloc[:0])
