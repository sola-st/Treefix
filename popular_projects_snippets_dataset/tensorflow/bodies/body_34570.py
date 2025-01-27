# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session() as session:
    x0 = constant_op.constant(5.0)
    x1 = constant_op.constant(10.0)
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=2).write(0, x0).write(1, x1)
    r0 = ta.read(0)
    # calculate (dr0/dx0, dr0/dx1).  since r0 = x0, gradients are (1, 0).
    grad_r0_x1 = gradients_impl.gradients(ys=[r0], xs=[x0, x1], grad_ys=[1.0])
    grad_r0_x1_vals = session.run(grad_r0_x1)
    self.assertAllEqual(grad_r0_x1_vals, [1.0, 0.0])
