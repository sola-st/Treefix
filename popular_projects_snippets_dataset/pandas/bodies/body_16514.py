# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# GH 12577
# pivot_table counts null into margin ('All')
# when margins=true and dropna=true

df = DataFrame({"a": [1, 2, 2, 2, 2, np.nan], "b": [3, 3, 4, 4, 4, 4]})
actual = crosstab(df.a, df.b, margins=True, dropna=True)
expected = DataFrame([[1, 0, 1], [1, 3, 4], [2, 3, 5]])
expected.index = Index([1.0, 2.0, "All"], name="a")
expected.columns = Index([3, 4, "All"], name="b")
tm.assert_frame_equal(actual, expected)
