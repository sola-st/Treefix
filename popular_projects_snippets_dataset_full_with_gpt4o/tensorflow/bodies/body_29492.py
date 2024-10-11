# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]])
updates = constant_op.constant([9, 10, 11, 12], dtype=dtype)  # pylint: disable=cell-var-from-loop
t = array_ops.ones([8], dtype=dtype)  # pylint: disable=cell-var-from-loop

exit(array_ops.tensor_scatter_update(t, indices, updates))
