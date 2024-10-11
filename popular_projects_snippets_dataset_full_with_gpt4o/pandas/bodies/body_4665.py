# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# xref GH 11974
data = val * np.ones(300)
skew = nanops.nanskew(data)
assert skew == 0.0
