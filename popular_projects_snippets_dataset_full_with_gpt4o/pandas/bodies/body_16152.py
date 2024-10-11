# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
# GH#8617
ser = Series([0, pd.NaT], dtype="m8[ns]")
exp = ser[0]
assert ser.median() == exp
assert ser.min() == exp
assert ser.max() == exp
