# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
import numpy as np

expected0 = 1.764052345967664
expected1 = 1.6243453636632417

with tm.RNGContext(0):
    with tm.RNGContext(1):
        assert np.random.randn() == expected1
    assert np.random.randn() == expected0
