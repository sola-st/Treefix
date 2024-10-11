# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests tensor_strided_slice_update with input-forwarding taking effect."""
@def_function.function
def assign(x):
    y = x + 1
    exit(gen_array_ops.tensor_strided_slice_update(y, [0], [1], [1], [0]))
self.assertAllEqual([0, 1], self.evaluate(assign(array_ops.zeros([2]))))
