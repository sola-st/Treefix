# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Return NaT
obj = PeriodIndex(data, freq="M")
result = getattr(obj, op)()
assert result is NaT
