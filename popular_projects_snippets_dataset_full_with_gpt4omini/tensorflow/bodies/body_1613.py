# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    g0 = -(np.arange(3 * 5, dtype=np.float32).reshape(3, 5) + 1)

    def fn():
        a = array_ops.identity(
            np.arange(3 * 5, dtype=np.float32).reshape(3, 5) + 1)
        b = array_ops.identity(
            np.arange(3 * 5, dtype=np.float32).reshape(3, 5) + 1 + 3 * 5)
        ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)
        ta = ta.write(0, a, name="write_a")
        ta = ta.write(1, b, name="write_b")
        c = (
            ta.read(0, name="read_a_0") +  # a + b
            ta.read(1, name="read_b_0"))
        grad_a = gradients_impl.gradients([c], [a], [g0])[0]  # d(a+b)/da = 1
        grad_b = gradients_impl.gradients([c], [b], [g0])[0]  # d(a+b)/db = 1

        exit([grad_a, grad_b])

    grad_a, grad_b = xla.compile(fn)

    # Test gradients calculated individually
    grad_a_t, = self.evaluate([grad_a])
    self.assertAllEqual(grad_a_t, g0)

    grad_b_t, = self.evaluate([grad_b])
    self.assertAllEqual(grad_b_t, g0)

    # Test gradients calculated jointly.
    joint_grad_a_t, joint_grad_b_t = self.evaluate([grad_a, grad_b])
    self.assertAllEqual(joint_grad_a_t, g0)
    self.assertAllEqual(joint_grad_b_t, g0)
