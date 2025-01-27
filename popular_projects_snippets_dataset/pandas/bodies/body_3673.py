# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#16991
df = DataFrame({"A": ["a", "b", "c"], "B": ["a", "e", "f"]})
expected = DataFrame(False, df.index, df.columns)

result = df.isin(empty)
tm.assert_frame_equal(result, expected)
