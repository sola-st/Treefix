# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
# We check that scalar and empty indices shapes work as well
shape = (2, 1, 3, 2)
for indices_shape in (), (0,), (2, 0), (2, 3):
    for dtype in _TEST_TYPES:
        for axis in range(len(shape)):
            params = self._buildParams(np.random.randn(*shape), dtype)
            indices = np.random.randint(shape[axis], size=indices_shape)
            with self.subTest(
                indices_shape=indices_shape,
                dtype=dtype,
                axis=axis,
                indices=indices):
                with backprop.GradientTape() as tape:
                    tf_params = constant_op.constant(params)
                    tf_indices = constant_op.constant(indices)
                    # Check that both positive and negative indices for axis work.
                    tf_axis = constant_op.constant(axis)
                    tape.watch(tf_params)
                    tape.watch(tf_indices)
                    tape.watch(tf_axis)
                    tf_negative_axis = constant_op.constant(-len(shape) + axis)
                    gather = array_ops.gather(tf_params, tf_indices, axis=tf_axis)
                    gather_negative_axis = array_ops.gather(
                        tf_params, tf_indices, axis=tf_negative_axis)
                    gather_value, gather_negative_axis_value = self.evaluate(
                        [gather, gather_negative_axis])
                    gather_np = np.take(params, indices, axis)
                    self.assertAllEqual(gather_np, gather_value)
                    self.assertAllEqual(gather_np, gather_negative_axis_value)
                    expected_shape = (
                        params.shape[:axis] + indices.shape + params.shape[axis + 1:])
                    self.assertEqual(expected_shape, gather.shape)
                    self.assertEqual(expected_shape, gather_negative_axis.shape)

                    # Test gradients
                    gather_grad = np.random.randn(
                        *gather.get_shape().as_list()).astype(dtype.as_numpy_dtype)
                    if dtype.is_complex:
                        gather_grad -= 1j * gather_grad
                params_grad, indices_grad, axis_grad = tape.gradient(
                    gather, [tf_params, tf_indices, tf_axis], gather_grad)
                self.assertIsNone(indices_grad)
                self.assertIsNone(axis_grad)
                if dtype.is_integer:
                    self.assertIsNone(params_grad)
                    continue
                # For axis 0, we are able to create an efficient IndexedSlices for
                # the gradient.
                if axis == 0:
                    self.assertEqual(type(params_grad), indexed_slices.IndexedSlices)
                    params_grad = ops.convert_to_tensor(params_grad)
                correct_params_grad = np.zeros(shape).astype(dtype.as_numpy_dtype)
                outer_dims = axis
                inner_dims = len(shape) - axis - 1
                gather_grad = gather_grad.reshape(shape[:axis] + (indices.size,) +
                                                  shape[axis + 1:])
                for source_index, dest_index in enumerate(indices.flat):
                    dest_slice = ((slice(None),) * outer_dims + (dest_index,) +
                                  (slice(None),) * inner_dims)
                    source_slice = ((slice(None),) * outer_dims + (source_index,) +
                                    (slice(None),) * inner_dims)
                    correct_params_grad[dest_slice] += gather_grad[source_slice]
                self.assertAllCloseAccordingToType(
                    correct_params_grad,
                    self.evaluate(params_grad),
                    atol=2e-6,
                    rtol=2e-6,
                )
