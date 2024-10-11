# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
"""This method is structured to be easily overridden by a child class."""
self._testLabelsPlaceholderScalar(
    expected_error_message="labels must be 1-D")
