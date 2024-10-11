# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#50453 pre-2.0 with mixed numeric/datetimes and errors="coerce"
#  the numeric entries would be coerced to NaT, was never clear exactly
#  why.
# mixed integers/datetimes
expected = Index([Timestamp(x) for x in arr], dtype="M8[ns]")
result = to_datetime(arr, errors="coerce", cache=cache)
tm.assert_index_equal(result, expected)

# GH#49037 pre-2.0 this raised, but it always worked with Series,
#  was never clear why it was disallowed
result = to_datetime(arr, errors="raise", cache=cache)
tm.assert_index_equal(result, expected)

result = DatetimeIndex(arr)
tm.assert_index_equal(result, expected)
