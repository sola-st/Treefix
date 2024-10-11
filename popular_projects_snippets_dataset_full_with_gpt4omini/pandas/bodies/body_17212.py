# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48293
df = DataFrame({None: [1], "b": 2, "c": 3})

result = df.pivot(columns="b", index=None)
expected = DataFrame({("c", 2): 3}, index=[1])
expected.columns.names = [None, "b"]
tm.assert_frame_equal(result, expected)

result = df.pivot(columns="b", index=None, values="c")
expected = DataFrame(3, index=[1], columns=Index([2], name="b"))
tm.assert_frame_equal(result, expected)
