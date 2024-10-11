# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
other = DataFrame({"A": [1, 0, 1, 0], "B": [1, 1, 0, 0]})
df = DataFrame([[1, 1], [1, 0], [0, 0]], columns=["A", "A"])
result = df.isin(other)
expected = DataFrame(False, index=df.index, columns=df.columns)
expected.loc[0] = True
expected.iloc[1, 1] = True
tm.assert_frame_equal(result, expected)
