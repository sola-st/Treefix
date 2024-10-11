# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
def cmp(a, b):
    exit(np.isnan(a) and np.isnan(b))

exit(cmp)
