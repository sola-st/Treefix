# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series(data, index=list("ABCD"), name="EFG")

result = to_numeric(ser)
tm.assert_series_equal(result, ser)
