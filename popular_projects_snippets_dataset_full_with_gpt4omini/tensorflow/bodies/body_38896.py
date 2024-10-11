# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=[2, 2, None])

    # Provided shape has wrong rank
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected shape rank at least 3, got 2"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array([[1, 2]]).astype(np.float32),
            grad_shape=[2, 2]).run()

    # Provided shape has wrong dim
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected shape dim 1 to be 2, got 3"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array([[[1, 2], [3, 4], [5, 6]]]).astype(np.float32),
            grad_shape=[2, 3, 2]).run()

    # Indices exceeded accumulator's shape's limits
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: index of slice 0 exceeded limits of shape;"
        " index is 3 exceeded 2"):
        q.apply_grad(
            grad_indices=[3],
            grad_values=np.array([[[1, 2], [3, 4]]]).astype(np.float32)).run()

    # Values' rank does not match shape
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected values rank at least 3, got 2"):
        q.apply_grad(
            grad_indices=[0, 1],
            grad_values=np.array([[1, 2], [3, 4]]).astype(np.float32)).run()

    # Values' dim does not match shape
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected values dim 1 to be 2, got 3"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array(
                [[[1, 2], [3, 4], [5, 6]]]).astype(np.float32)).run()

    # First successful gradient creates additional constraints
    # Shape will be additionally be constrained to [None,2,2,2] hereafter.
    q.apply_grad(
        grad_indices=[0],
        grad_values=np.array(
            [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]).astype(np.float32)).run()

    # Values' rank does not match accumulated gradient
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected values rank 4, got 3"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array([[[1, 2], [3, 4]]]).astype(np.float32)).run()

    # Values' dim does not match accumulated gradient
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected values dim 3 to be 2, got 3"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array(
                [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]]).astype(
                    np.float32)).run()

    # After take grad, constraints on accumulated gradient are removed
    self.evaluate(q.take_grad(1))

    # First successful gradient imposes new constraints.
    # Hereafter, shape will additionally constrained to [None,2,2,3]
    q.apply_grad(
        grad_indices=[0],
        grad_values=np.array(
            [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]]).astype(
                np.float32),
        local_step=1).run()

    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch: expected values dim 3 to be 3, got 2"):
        q.apply_grad(
            grad_indices=[0],
            grad_values=np.array(
                [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]).astype(np.float32),
            local_step=1).run()
