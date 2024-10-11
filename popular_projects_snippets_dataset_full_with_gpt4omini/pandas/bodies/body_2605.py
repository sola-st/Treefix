# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# this is actually mostly a test of lib.maybe_convert_objects
# #2845
df = DataFrame({"A": [2**63 - 1]})
result = df["A"]
expected = Series(np.asarray([2**63 - 1], np.int64), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [2**63]})
result = df["A"]
expected = Series(np.asarray([2**63], np.uint64), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [datetime(2005, 1, 1), True]})
result = df["A"]
expected = Series(
    np.asarray([datetime(2005, 1, 1), True], np.object_), name="A"
)
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [None, 1]})
result = df["A"]
expected = Series(np.asarray([np.nan, 1], np.float_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0, 2]})
result = df["A"]
expected = Series(np.asarray([1.0, 2], np.float_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0 + 2.0j, 3]})
result = df["A"]
expected = Series(np.asarray([1.0 + 2.0j, 3], np.complex_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0 + 2.0j, 3.0]})
result = df["A"]
expected = Series(np.asarray([1.0 + 2.0j, 3.0], np.complex_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0 + 2.0j, True]})
result = df["A"]
expected = Series(np.asarray([1.0 + 2.0j, True], np.object_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0, None]})
result = df["A"]
expected = Series(np.asarray([1.0, np.nan], np.float_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [1.0 + 2.0j, None]})
result = df["A"]
expected = Series(np.asarray([1.0 + 2.0j, np.nan], np.complex_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [2.0, 1, True, None]})
result = df["A"]
expected = Series(np.asarray([2.0, 1, True, None], np.object_), name="A")
tm.assert_series_equal(result, expected)

df = DataFrame({"A": [2.0, 1, datetime(2006, 1, 1), None]})
result = df["A"]
expected = Series(
    np.asarray([2.0, 1, datetime(2006, 1, 1), None], np.object_), name="A"
)
tm.assert_series_equal(result, expected)
