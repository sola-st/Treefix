# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session(), self.test_scope():

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)
        c0 = constant_op.constant([4.0, 5.0])
        w0 = ta.write(0, c0)
        r0 = w0.read(0)

        exit([c0, r0])

    c0, r0 = xla.compile(fn)

    self.assertAllEqual(c0.get_shape(), r0.get_shape())

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)
        c1 = constant_op.constant([6.0, 7.0])
        w0 = ta.write(0, c0)
        w1 = w0.write(1, c1)
        r0 = w1.read(0)
        r1 = w1.read(1)

        exit([r0, c1, r1])

    [r0, c1, r1] = xla.compile(fn)

    self.assertAllEqual(c0.get_shape(), r0.get_shape())
    self.assertAllEqual(c1.get_shape(), r1.get_shape())

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, tensor_array_name="foo", size=3)
        w0 = ta.write(0, c0)
        c2 = constant_op.constant([4.0, 5.0, 6.0])
        exit(w0.write(0, c2).flow)

    with self.assertRaises(ValueError):
        self.evaluate(xla.compile(fn))
