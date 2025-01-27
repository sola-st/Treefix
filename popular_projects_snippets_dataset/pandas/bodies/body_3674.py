# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
df = DataFrame({"A": ["a", "b", "c"], "B": ["a", "e", "f"]})
d = {"A": ["a"]}

expected = DataFrame(False, df.index, df.columns)
expected.loc[0, "A"] = True

result = df.isin(d)
tm.assert_frame_equal(result, expected)

# non unique columns
df = DataFrame({"A": ["a", "b", "c"], "B": ["a", "e", "f"]})
df.columns = ["A", "A"]
expected = DataFrame(False, df.index, df.columns)
expected.loc[0, "A"] = True
result = df.isin(d)
tm.assert_frame_equal(result, expected)
