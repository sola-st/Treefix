# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    convert = _make_converter(tf_dtype)

    # Split an empty vector
    ta = _make_ta(3, "foo", dtype=tf_dtype)
    lengths = constant_op.constant([0, 0, 0])
    w0 = ta.split(convert([]), lengths=lengths)
    r0 = w0.read(0)
    r1 = w0.read(1)
    r2 = w0.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert([]), d0)
    self.assertAllEqual(convert([]), d1)
    self.assertAllEqual(convert([]), d2)

    # Split a vector
    lengths = constant_op.constant([2, 0, 1])
    w0 = ta.split(convert([1.0, 2.0, 3.0]), lengths=lengths)
    r0 = w0.read(0)
    r1 = w0.read(1)
    r2 = w0.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert([1.0, 2.0]), d0)
    self.assertAllEqual(convert([]), d1)
    self.assertAllEqual(convert([3.0]), d2)

    # Split a matrix
    lengths = constant_op.constant([2, 0, 1])
    w0 = ta.split(
        convert([[1.0, 101.0], [2.0, 201.0], [3.0, 301.0]]), lengths=lengths)
    r0 = w0.read(0)
    r1 = w0.read(1)
    r2 = w0.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert([[1.0, 101.0], [2.0, 201.0]]), d0)
    self.assertAllEqual(convert([]).reshape(0, 2), d1)
    self.assertAllEqual(convert([[3.0, 301.0]]), d2)
