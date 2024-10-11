# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
"""Ensures we return the right thing for multiple NaNs."""
one_with_nans = np.array(
    [1.0, float("nan"), float("nan")], dtype=np.float32)
np.testing.assert_equal(
    np.argmin(one_with_nans.astype(float_type)), np.argmin(one_with_nans))
