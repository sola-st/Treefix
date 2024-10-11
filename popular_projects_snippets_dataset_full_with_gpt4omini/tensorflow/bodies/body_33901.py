# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/scatter_nd_ops_test.py
"""This tests scatter_add using indices that repeat."""
self._ScatterRepeatIndicesTest(_NumpyMin, state_ops.scatter_nd_min)
self._ScatterRepeatIndicesTest(_NumpyMax, state_ops.scatter_nd_max)
