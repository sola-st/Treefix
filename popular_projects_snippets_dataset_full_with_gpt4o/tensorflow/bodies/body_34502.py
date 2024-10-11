# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)

    empty_element = np.zeros((0, 1), dtype=np.float32)
    w0 = ta.write(0, empty_element)
    w1 = w0.write(1, empty_element)
    w2 = w1.write(2, empty_element)

    c0 = w2.stack()

    c0 = self.evaluate(c0)
    self.assertAllEqual([3, 0, 1], c0.shape)
