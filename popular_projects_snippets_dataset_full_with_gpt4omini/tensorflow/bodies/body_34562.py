# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)
    c0 = constant_op.constant([4.0, 5.0])
    w0 = ta.write(0, c0)
    r0 = w0.read(0)
    self.assertAllEqual(c0.get_shape(), r0.get_shape())

    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)
    c1 = constant_op.constant([6.0, 7.0])
    w1 = w0.write(1, c1)
    r0 = w1.read(0)
    r1 = w1.read(1)
    self.assertAllEqual(c0.get_shape(), r0.get_shape())
    self.assertAllEqual(c1.get_shape(), r1.get_shape())

    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)
    c2 = constant_op.constant([4.0, 5.0, 6.0])
    with self.assertRaises(ValueError):
        w0.write(0, c2)
