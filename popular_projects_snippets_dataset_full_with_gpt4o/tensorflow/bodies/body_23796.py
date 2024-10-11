# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
"""Ensures we return the right thing for negative infinities."""
inf = np.array([float("-inf")], dtype=np.float32)
np.testing.assert_equal(np.argmax(inf.astype(float_type)), np.argmax(inf))
