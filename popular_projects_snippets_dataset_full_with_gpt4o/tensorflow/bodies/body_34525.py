# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, tensor_array_name="foo", size=3)

    with self.assertRaisesOpError(
        "Could not write to TensorArray index 2 because "
        "it has already been written to."):
        self.evaluate(ta.write(2, 3.0).write(2, 3.0).flow)
