# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    h1 = tensor_array_ops.TensorArray(
        size=1, dtype=dtypes.float32, tensor_array_name="foo")
    w1 = h1.write(0, 4.0)
    r1 = w1.read(0)

    h2 = tensor_array_ops.TensorArray(
        size=1, dtype=dtypes.float32, tensor_array_name="bar")

    w2 = h2.write(0, 5.0)
    r2 = w2.read(0)
    r = r1 + r2
    val = self.evaluate(r)
    self.assertAllClose(9.0, val)
