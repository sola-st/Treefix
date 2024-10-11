# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
with self.session() as session, self.test_scope():
    convert = _make_converter(tf_dtype)

    def fn():
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)

        # Split an empty vector.
        lengths = constant_op.constant([0, 0, 0])
        w0 = ta.split(convert([]), lengths=lengths)
        r0 = w0.read(0)
        r1 = w0.read(1)
        r2 = w0.read(2)
        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))

    self.assertAllEqual(convert([]), d0)
    self.assertAllEqual(convert([]), d1)
    self.assertAllEqual(convert([]), d2)

    def fn():
        # Split a vector.
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)
        lengths = constant_op.constant([1, 1, 1])
        w0 = ta.split(convert([1.0, 2.0, 3.0]), lengths=lengths)
        r0 = w0.read(0)
        r1 = w0.read(1)
        r2 = w0.read(2)
        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))

    self.assertAllEqual(convert([1.0]), d0)
    self.assertAllEqual(convert([2.0]), d1)
    self.assertAllEqual(convert([3.0]), d2)

    def fn():
        # Split a matrix.
        ta = tensor_array_ops.TensorArray(
            dtype=tf_dtype, tensor_array_name="foo", size=3)
        lengths = constant_op.constant([1, 1, 1])
        w0 = ta.split(
            convert([[1.0, 101.0], [2.0, 121.0], [3.0, 127.0]]),
            lengths=lengths)
        r0 = w0.read(0)
        r1 = w0.read(1)
        r2 = w0.read(2)
        exit([r0, r1, r2])

    d0, d1, d2 = self.evaluate(xla.compile(fn))
    self.assertAllEqual(convert([[1.0, 101.0]]), d0)
    self.assertAllEqual(convert([[2.0, 121.0]]), d1)
    self.assertAllEqual(convert([[3.0, 127.0]]), d2)
