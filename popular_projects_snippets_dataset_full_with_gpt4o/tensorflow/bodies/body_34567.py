# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3,
        infer_shape=True)
    c0 = array_ops.placeholder(dtypes.float32)
    w0 = ta.write(0, c0)
    r0 = w0.read(0)
    self.assertAllEqual(r0.get_shape(), tensor_shape.unknown_shape())
