# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3,
        infer_shape=False)

    w0 = ta.write(0, [[4.0, 5.0]])
    w1 = w0.write(1, [[1.0]])
    w2 = w1.write(2, -3.0)

    r0 = w2.read(0)
    r1 = w2.read(1)
    r2 = w2.read(2)

    d0, d1, d2 = self.evaluate([r0, r1, r2])
    self.assertAllEqual([[4.0, 5.0]], d0)
    self.assertAllEqual([[1.0]], d1)
    self.assertAllEqual(-3.0, d2)
