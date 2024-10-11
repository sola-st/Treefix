# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# integer div, but deal with the 0's (GH#9144)
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})

first = Series([1.0, 1.0, 1.0, 1.0])
second = Series([np.nan, np.nan, np.nan, 1])
expected = pd.DataFrame({"first": first, "second": second})

with np.errstate(all="ignore"):
    arr = df.values.astype("float") / df.values
result = pd.DataFrame(arr, index=df.index, columns=df.columns)
tm.assert_frame_equal(result, expected)
