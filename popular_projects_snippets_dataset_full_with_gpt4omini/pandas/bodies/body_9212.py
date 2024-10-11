# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_replace.py
# GH 31720

ser = pd.Series([1, 2, 3], dtype="category")
result = ser.replace(to_replace, value)
expected = pd.Series(expected, dtype="category")
ser.replace(to_replace, value, inplace=True)

if flip_categories:
    expected = expected.cat.set_categories(expected.cat.categories[::-1])

tm.assert_series_equal(expected, result, check_category_order=False)
tm.assert_series_equal(expected, ser, check_category_order=False)
