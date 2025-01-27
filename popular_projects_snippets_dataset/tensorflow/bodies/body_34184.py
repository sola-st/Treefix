# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
# list_kernels.cc in tf/core/kernels raises InvalidArgumentError, and
# tf_ops_n_z.cc in tf/compiler/mlir/tf/ir raises UnknownError.
with self.assertRaises((errors.InvalidArgumentError, errors.UnknownError)):
    l = list_ops.tensor_list_reserve(
        element_dtype=dtypes.float32,
        element_shape=[2, 3],
        num_elements=constant_op.constant([1, 1]))
    self.evaluate(l)
