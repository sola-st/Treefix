# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that the generated numbers are the same as the old random_ops.py.

    The CPU version.
    """
self._sameAsOldRandomOps("/device:CPU:0", FLOATS)
