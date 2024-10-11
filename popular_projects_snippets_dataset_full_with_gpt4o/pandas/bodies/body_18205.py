# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#3590, modulo as ints
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})

# this is technically wrong, as the integer portion is coerced to float
# ###
first = Series([0, 0, 0, 0], dtype="float64")
second = Series([np.nan, np.nan, np.nan, 0])
expected = pd.DataFrame({"first": first, "second": second})

# numpy has a slightly different (wrong) treatment
with np.errstate(all="ignore"):
    arr = df.values % df.values
result2 = pd.DataFrame(arr, index=df.index, columns=df.columns, dtype="float64")
result2.iloc[0:3, 1] = np.nan
tm.assert_frame_equal(result2, expected)
