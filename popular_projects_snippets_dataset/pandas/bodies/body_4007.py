# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
df = DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])

data = np.random.randn(10)
df1 = DataFrame.from_records(df, index=data)
tm.assert_index_equal(df1.index, Index(data))
