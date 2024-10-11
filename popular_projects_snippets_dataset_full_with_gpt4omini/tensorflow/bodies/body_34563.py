# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=6)

    c0 = array_ops.placeholder(dtypes.float32, [None, None, None, 3])
    w0 = ta.write(0, c0)
    r0 = w0.read(0)
    self.assertAllEqual([None, None, None, 3], r0.get_shape().as_list())

    c1 = array_ops.placeholder(dtypes.float32, [None, None, None, 3])
    w1 = w0.write(1, c1)
    r1 = w1.read(0)
    self.assertAllEqual([None, None, None, 3], r1.get_shape().as_list())

    # Writing less specific shape (doesn't change type.)
    c2 = array_ops.placeholder(dtypes.float32, [None, None, None, None])
    w2 = w1.write(2, c2)
    r2 = w2.read(0)
    self.assertAllEqual([None, None, None, 3], r2.get_shape().as_list())

    # Writing more specific shape in one dimension and less specific in
    # another.
    c3 = array_ops.placeholder(dtypes.float32, [None, None, 2, None])
    w3 = w2.write(3, c3)
    r3 = w3.read(0)
    self.assertAllEqual([None, None, 2, 3], r3.get_shape().as_list())

    # Writing partly defined shape using TensorArray.scatter.
    c4 = array_ops.placeholder(dtypes.float32, [2, None, 4, 2, 3])
    w4 = w3.scatter([4, 5], c4)
    r4 = w4.read(0)
    self.assertAllEqual([None, 4, 2, 3], r4.get_shape().as_list())

    # Writing fully defined shape using TensorArray.split.
    c5 = array_ops.placeholder(dtypes.float32, [10, 4, 2, 3])
    w5 = w4.split(c5, constant_op.constant([5, 5]))
    r5 = w5.read(0)
    self.assertAllEqual([5, 4, 2, 3], r5.get_shape().as_list())
