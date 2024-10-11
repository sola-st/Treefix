# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH22305
expected = Index([NaT, NaT], dtype="datetime64[ns]")
result = to_datetime([unique_nulls_fixture, unique_nulls_fixture2], cache=cache)
tm.assert_index_equal(result, expected)
