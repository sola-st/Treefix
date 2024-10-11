# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Return NaT
obj = TimedeltaIndex([])
assert getattr(obj, op)() is NaT

obj = TimedeltaIndex([NaT])
assert getattr(obj, op)() is NaT

obj = TimedeltaIndex([NaT, NaT, NaT])
assert getattr(obj, op)() is NaT
