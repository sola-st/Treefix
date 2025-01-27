# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
columns = MultiIndex.from_tuples([("foo", 1), ("foo", 2), ("bar", 1)])
df = DataFrame(np.random.randn(3, 3), columns=columns)

result = df.set_index(df.columns[0])

expected = df.iloc[:, 1:]
expected.index = df.iloc[:, 0].values
expected.index.names = [df.columns[0]]
tm.assert_frame_equal(result, expected)
