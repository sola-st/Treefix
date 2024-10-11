# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([]))

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Input indices should be vector"):
        q.apply_grad(grad_indices=0, grad_values=[1.0], grad_shape=[]).run()

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Input indices should be vector"):
        q.apply_grad(grad_indices=0, grad_values=[1.0]).run()

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Values cannot be 0-dimensional."):
        q.apply_grad(grad_indices=[0], grad_values=1.0, grad_shape=[]).run()

    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Values cannot be 0-dimensional."):
        q.apply_grad(grad_indices=[0], grad_values=1.0).run()

    # The right way to apply a scalar
    q.apply_grad(grad_indices=[0], grad_values=[1.0], grad_shape=[]).run()
    q.apply_grad(grad_indices=[0], grad_values=[1.0]).run()
