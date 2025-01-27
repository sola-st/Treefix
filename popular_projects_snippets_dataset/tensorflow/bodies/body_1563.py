# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    convert = _make_converter(tf_dtype)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)

        # Unpack a vector into scalars
        w0 = ta.unstack(convert([1.0, 2.0, 3.0]))
        r0 = w0.read(0)
        r1 = w0.read(1)
        r2 = w0.read(2)

        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))
    self.assertAllEqual(convert(1.0), d0)
    self.assertAllEqual(convert(2.0), d1)
    self.assertAllEqual(convert(3.0), d2)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)

        # Unpack a matrix into vectors.
        w1 = ta.unstack(
            convert([[1.0, 1.03125], [2.0, 2.03125], [3.0, 3.03125]]))
        r0 = w1.read(0)
        r1 = w1.read(1)
        r2 = w1.read(2)
        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))

    self.assertAllEqual(convert([1.0, 1.03125]), d0)
    self.assertAllEqual(convert([2.0, 2.03125]), d1)
    self.assertAllEqual(convert([3.0, 3.03125]), d2)

    def fn():
        # Reset ta because we're going to change the shape, else shape
        # inference will throw an error.
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)

        # Try unpacking an empty matrix, which should not cause an error.
        w2 = ta.unstack(convert([[], [], []]))
        r0 = w2.read(0)
        r1 = w2.read(1)
        r2 = w2.read(2)
        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))
    self.assertAllEqual(convert([]), d0)
    self.assertAllEqual(convert([]), d1)
    self.assertAllEqual(convert([]), d2)
