# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#3590, modulo as ints
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})

result = df % 0
expected = pd.DataFrame(np.nan, index=df.index, columns=df.columns)
tm.assert_frame_equal(result, expected)

# numpy has a slightly different (wrong) treatment
with np.errstate(all="ignore"):
    arr = df.values.astype("float64") % 0
result2 = pd.DataFrame(arr, index=df.index, columns=df.columns)
tm.assert_frame_equal(result2, expected)
