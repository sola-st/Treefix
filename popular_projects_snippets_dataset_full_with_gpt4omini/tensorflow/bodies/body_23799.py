# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
"""Ensures we return the right thing for positive infinities."""
inf = np.array([float("inf")], dtype=np.float32)
np.testing.assert_equal(np.argmin(inf.astype(float_type)), np.argmin(inf))
