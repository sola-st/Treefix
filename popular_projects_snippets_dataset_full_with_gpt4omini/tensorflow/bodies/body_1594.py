# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    c = lambda x: np.array(x, dtype=dtype)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.as_dtype(dtype),
            tensor_array_name="foo",
            size=3,
            infer_shape=False)

        value_0 = constant_op.constant(c([[4.0, 5.0]]))
        value_1 = constant_op.constant(c([[3.0, 3.5]]))

        w0 = ta.write(0, value_0)
        w1 = w0.write(1, value_1)
        r0 = w1.read(0)
        r1 = w1.read(1)
        r0_2 = w1.read(0)

        # Test individual components' gradients
        grad_just_r0 = gradients_impl.gradients(
            ys=[r0], xs=[value_0], grad_ys=[c([[2.0, 3.0]])])
        grad_r0_r0_2 = gradients_impl.gradients(
            ys=[r0, r0_2],
            xs=[value_0],
            grad_ys=[c([[2.0, 3.0]]), c([[1.0, -1.0]])])
        grad_just_r1 = gradients_impl.gradients(
            ys=[r1], xs=[value_1], grad_ys=[c([[-2.0, -4.0]])])
        # Test combined gradients
        grad = gradients_impl.gradients(
            ys=[r0, r0_2, r1],
            xs=[value_0, value_1],
            grad_ys=[c([[2.0, 3.0]]),
                     c([[1.0, -1.0]]),
                     c([[-2.0, -10.0]])])

        exit([grad_just_r0, grad_r0_r0_2, grad_just_r1, grad])

    [grad_just_r0_vals, grad_r0_r0_2_vals, grad_just_r1_vals,
     grad_vals] = self.evaluate(xla.compile(fn))

    self.assertAllEqual(c([[2.0, 3.0]]), grad_just_r0_vals[0])

    self.assertAllEqual(c([[3.0, 2.0]]), grad_r0_r0_2_vals[0])

    self.assertAllEqual(c([[-2.0, -4.0]]), grad_just_r1_vals[0])

    self.assertEqual(len(grad_vals), 2)
    self.assertAllEqual(c([[3.0, 2.0]]), grad_vals[0])
    self.assertAllEqual(c([[-2.0, -10.0]]), grad_vals[1])
