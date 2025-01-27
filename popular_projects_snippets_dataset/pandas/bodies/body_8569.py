# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
idx = date_range(start="2000-01-01", periods=1, freq="A", name="TEST")
assert idx.name == "TEST"
