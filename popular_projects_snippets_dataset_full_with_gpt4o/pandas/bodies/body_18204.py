# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#3590, modulo as ints
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})
# this is technically wrong, as the integer portion is coerced to float
first = Series([0, 0, 0, 0])
if not using_array_manager:
    # INFO(ArrayManager) BlockManager doesn't preserve dtype per column
    # while ArrayManager performs op column-wisedoes and thus preserves
    # dtype if possible
    first = first.astype("float64")
second = Series([np.nan, np.nan, np.nan, 0])
expected = pd.DataFrame({"first": first, "second": second})
result = df % df
tm.assert_frame_equal(result, expected)

# GH#38939 If we dont pass copy=False, df is consolidated and
#  result["first"] is float64 instead of int64
df = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]}, copy=False)
first = Series([0, 0, 0, 0], dtype="int64")
second = Series([np.nan, np.nan, np.nan, 0])
expected = pd.DataFrame({"first": first, "second": second})
result = df % df
tm.assert_frame_equal(result, expected)
