# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError,
                             errors_impl.InternalError),
                            "Index out of range|expected <"):
    sparse_data = sparse_tensor_lib.SparseTensor(
        constant_op.constant([[804, 7450], [48245, 2577]], dtypes.int64),
        constant_op.constant([1, 1], dtypes.int64),
        constant_op.constant([812, 390], dtypes.int64))
    self.evaluate(sets.set_size(sparse_data, validate_indices=False))
