# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Return NaT
obj = DatetimeIndex([])
assert isna(getattr(obj, op)())

obj = DatetimeIndex([NaT])
assert isna(getattr(obj, op)())

obj = DatetimeIndex([NaT, NaT, NaT])
assert isna(getattr(obj, op)())
