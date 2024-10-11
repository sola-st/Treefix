# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)

        w0 = ta.write(0, [[4.0]])
        w1 = w0.write(1, [[1.0]])
        w2 = w1.write(2, [[-3.0]])

        g_ta = w2.grad("grad")

        g_w0 = g_ta.write(0, [[5.0]])
        g_w1 = g_w0.write(1, [[2.0]])
        g_w2 = g_w1.write(2, [[-2.0]])

        r0 = w2.read(0)
        r1 = w2.read(1)
        r2 = w2.read(2)

        g_r0 = g_w2.read(0)
        g_r1 = g_w2.read(1)
        g_r2 = g_w2.read(2)

        exit([r0, r1, r2, g_r0, g_r1, g_r2])

    d0, d1, d2, g_d0, g_d1, g_d2 = self.evaluate(xla.compile(fn))
    self.assertAllEqual([[4.0]], d0)
    self.assertAllEqual([[1.0]], d1)
    self.assertAllEqual([[-3.0]], d2)
    self.assertAllEqual([[5.0]], g_d0)
    self.assertAllEqual([[2.0]], g_d1)
    self.assertAllEqual([[-2.0]], g_d2)
