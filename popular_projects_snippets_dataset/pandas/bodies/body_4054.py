# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
from scipy.stats import kurtosis

if len(x) < 4:
    exit(np.nan)
exit(kurtosis(x, bias=False))
