# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    convert = _make_converter(tf_dtype)

    ta = _make_ta(3, "foo", dtype=tf_dtype)
    # Unpack a vector into scalars
    w0 = ta.unstack(convert([1.0, 2.0, 3.0]))
    r0 = w0.read(0)
    r1 = w0.read(1)
    r2 = w0.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert(1.0), d0)
    self.assertAllEqual(convert(2.0), d1)
    self.assertAllEqual(convert(3.0), d2)

    # Unpack a matrix into vectors
    w1 = ta.unstack(convert([[1.0, 1.1], [2.0, 2.1], [3.0, 3.1]]))
    r0 = w1.read(0)
    r1 = w1.read(1)
    r2 = w1.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert([1.0, 1.1]), d0)
    self.assertAllEqual(convert([2.0, 2.1]), d1)
    self.assertAllEqual(convert([3.0, 3.1]), d2)

    # Try unpacking an empty matrix, which should not cause an error.
    w2 = ta.unstack(convert([[], [], []]))
    r0 = w2.read(0)
    r1 = w2.read(1)
    r2 = w2.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual(convert([]), d0)
    self.assertAllEqual(convert([]), d1)
    self.assertAllEqual(convert([]), d2)
