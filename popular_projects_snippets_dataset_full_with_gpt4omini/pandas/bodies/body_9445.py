# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_cumulative.py
# GH#50297
arr = TimedeltaArray._from_sequence_not_strict(["1D", "2D"])
result = arr._accumulate("cumsum")
expected = TimedeltaArray._from_sequence_not_strict(["1D", "3D"])
tm.assert_timedelta_array_equal(result, expected)
