# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
if test_util.is_gpu_available():
    self.skipTest("Duplicate indices scatter is non-deterministic on GPU")
a = array_ops.zeros([10, 1])
b = array_ops.tensor_scatter_update(a, [[5], [5]], [[4], [8]])
self.assertAllEqual(
    b,
    constant_op.constant([[0.], [0.], [0.], [0.], [0.], [8.], [0.], [0.],
                          [0.], [0.]]))
