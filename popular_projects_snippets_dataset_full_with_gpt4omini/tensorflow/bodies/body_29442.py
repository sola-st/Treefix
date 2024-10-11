# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
"""This tests scatter_add using indices that repeat."""
self._ScatterRepeatIndicesTest(_NumpyAdd, state_ops.scatter_nd_add)
self._ScatterRepeatIndicesTest(_NumpySub, state_ops.scatter_nd_sub)
