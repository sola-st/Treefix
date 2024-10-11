# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
for dtype in GRADIENT_TESTS_DTYPES:
    with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
        indices = constant_op.constant([[[0, 1], [1, 0]], [[0, 0], [1, 1]]],
                                       dtype=dtypes.int32)
        updates = constant_op.constant([[[5, 7], [2, 4]], [[1, 3], [6, 8]]],
                                       dtype=dtype)
        tape.watch(updates)
        shape = constant_op.constant([2, 2, 2], dtype=dtypes.int32)
        input_ = array_ops.zeros(shape, dtype=dtype)
        tape.watch(input_)
        outputs = self.scatter_nd(indices, updates, shape, input_)

        grad_vals = constant_op.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                                         dtype=dtype)
        updates_grad, input_grad = tape.gradient([outputs], [updates, input_],
                                                 [grad_vals])
    expected_updates_grad = np.array([[[3, 4], [5, 6]], [[1, 2], [7, 8]]],
                                     dtype=dtype.as_numpy_dtype)
    expected_input_grad = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                                   dtype=dtype.as_numpy_dtype)
    self.assertAllEqual(expected_updates_grad, self.evaluate(updates_grad))
    if self.non_aliasing_add_test:
        self.assertAllEqual(expected_input_grad, self.evaluate(input_grad))
