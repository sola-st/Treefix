# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
empty = Series()
empty2 = Series(input_class())

# these are Index() and RangeIndex() which don't compare type equal
# but are just .equals
tm.assert_series_equal(empty, empty2, check_index_type=False)

# With explicit dtype:
empty = Series(dtype="float64")
empty2 = Series(input_class(), dtype="float64")
tm.assert_series_equal(empty, empty2, check_index_type=False)

# GH 18515 : with dtype=category:
empty = Series(dtype="category")
empty2 = Series(input_class(), dtype="category")
tm.assert_series_equal(empty, empty2, check_index_type=False)

if input_class is not list:
    # With index:
    empty = Series(index=range(10))
    empty2 = Series(input_class(), index=range(10))
    tm.assert_series_equal(empty, empty2)

    # With index and dtype float64:
    empty = Series(np.nan, index=range(10))
    empty2 = Series(input_class(), index=range(10), dtype="float64")
    tm.assert_series_equal(empty, empty2)

    # GH 19853 : with empty string, index and dtype str
    empty = Series("", dtype=str, index=range(3))
    empty2 = Series("", index=range(3))
    tm.assert_series_equal(empty, empty2)
