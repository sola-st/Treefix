# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
expected = {"over": "warn", "divide": "warn", "invalid": "warn", "under": "ignore"}
import numpy as np

# The error state should be unchanged after that import.
assert np.geterr() == expected
