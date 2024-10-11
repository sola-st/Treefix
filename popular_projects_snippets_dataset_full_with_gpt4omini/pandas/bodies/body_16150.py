# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
# GH#31746
ser = Series(["a", "b"], dtype="string")
res_operation_serie = getattr(ser, operation)()
assert res_operation_serie == expected
