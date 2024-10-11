# Extracted from ./data/repos/pandas/pandas/tests/base/test_unique.py
# GH37566
ser = pd.Series(["yes", "yes", pd.NA, np.nan, None, pd.NaT])
res = ser.nunique(dropna)
assert res == 1 if dropna else 5
