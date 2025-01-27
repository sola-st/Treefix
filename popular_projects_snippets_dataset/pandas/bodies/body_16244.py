# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#41805
ser = Series([None], dtype="interval[datetime64[ns]]")
assert ser.isna().all()
assert ser.dtype == "interval[datetime64[ns], right]"
