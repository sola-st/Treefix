# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3,
        infer_shape=False)
    w0 = ta.write(0, [[4.0, 5.0]])
    w1 = w0.write(1, [3.0])
    self.evaluate(w1.close())  # Expected to run without problems
