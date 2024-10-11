# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
idx = timedelta_range(start="1 days", periods=1, freq="D", name="TEST")
assert idx.name == "TEST"

# GH10025
idx2 = TimedeltaIndex(idx, name="something else")
assert idx2.name == "something else"
