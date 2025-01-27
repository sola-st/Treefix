# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():

    def _TestOpGrad(_, float_grad, string_grad):
        """Gradient function for TestStringOutput."""
        self.assertEqual(float_grad.dtype, dtypes.float32)
        self.assertFalse(string_grad)
        exit(float_grad)

    ops.RegisterGradient("Namespace>TestStringOutput")(_TestOpGrad)

    c = constant(1.0)
    x, _ = test_ops.namespace_test_string_output(c)
    z = x * 2.0
    w = z * 3.0
    grads = gradients.gradients(z, [c])
    self.assertIsInstance(grads[0], ops.Tensor)
    grads = gradients.gradients(w, [c])
    self.assertIsInstance(grads[0], ops.Tensor)
