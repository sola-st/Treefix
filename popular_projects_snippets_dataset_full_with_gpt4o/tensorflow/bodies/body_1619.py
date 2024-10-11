# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)
        x = constant_op.constant([2.0, 3.0])
        w = ta.unstack(x)
        r0 = w.read(0)
        # Calculate (dr0/dx0, dr0/dx1).  since r0 = x0, gradients are (1, 0).
        exit(gradients_impl.gradients(ys=[r0], xs=[x], grad_ys=[1.0]))

    grad_r0_vals = self.evaluate(xla.compile(fn))[0]
    self.assertAllEqual(grad_r0_vals, [1.0, 0.0])
