# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([3, 3]))

    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Input indices should be vector but received shape:"):
        q.apply_grad(
            grad_indices=[[0, 1], [1, 0]],
            grad_values=np.array([1, 2]).astype(np.float32)).run()
