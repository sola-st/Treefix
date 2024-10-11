# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_unique.py
# GH#18051
cat = Categorical([])
ser = Series(cat)
result = ser.unique()
tm.assert_categorical_equal(result, cat)

cat = Categorical([np.nan])
ser = Series(cat)
result = ser.unique()
tm.assert_categorical_equal(result, cat)
