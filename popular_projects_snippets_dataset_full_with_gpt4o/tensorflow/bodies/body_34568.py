# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session() as session:
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)
    x = constant_op.constant([2.0, 3.0])
    w = ta.unstack(x)
    r0 = w.read(0)
    # calculate (dr0/dx0, dr0/dx1).  since r0 = x0, gradients are (1, 0).
    grad_r0 = gradients_impl.gradients(ys=[r0], xs=[x], grad_ys=[1.0])
    grad_r0_vals = session.run(grad_r0)[0]
    self.assertAllEqual(grad_r0_vals, [1.0, 0.0])
