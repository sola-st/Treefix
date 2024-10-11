# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=2,
        clear_after_read=False)

    value_0 = constant_op.constant([-1.0, 1.0])
    value_1 = constant_op.constant([-10.0, 10.0])

    w0 = ta.write(0, value_0)
    w1 = w0.write(1, value_1)
    p0 = w1.stack()
    r0 = w1.read(0)
    s0 = w1.concat()

    # Test gradient accumulation between read(0), pack(), and concat()
    with ops.control_dependencies([p0, r0, s0]):
        grad_r = gradients_impl.gradients(
            ys=[p0, r0, s0],
            xs=[value_0, value_1],
            grad_ys=[
                [[2.0, 3.0], [4.0, 5.0]],  # pack gradient
                [-0.5, 1.5],  # read(0) gradient
                [20.0, 30.0, 40.0, 50.0]
            ])  # concat gradient
    grad_vals = self.evaluate(grad_r)  # 2 + 2 entries

    self.assertAllClose([2.0 - 0.5 + 20.0, 3.0 + 1.5 + 30.0], grad_vals[0])
    self.assertAllEqual([4.0 + 40.0, 5.0 + 50.0], grad_vals[1])
