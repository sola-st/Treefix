# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
"""Tests random_poisson_v2() for all supported dtype combinations."""
with self.cached_session():
    for lam_dt in _SUPPORTED_DTYPES:
        for out_dt in _SUPPORTED_DTYPES:
            random_ops.random_poisson(
                constant_op.constant([1], dtype=lam_dt), [10],
                dtype=out_dt).eval()
