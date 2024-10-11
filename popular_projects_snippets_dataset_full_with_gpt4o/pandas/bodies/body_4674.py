# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# xref GH 11974
data = val * np.ones(300)
kurt = nanops.nankurt(data)
assert kurt == 0.0
