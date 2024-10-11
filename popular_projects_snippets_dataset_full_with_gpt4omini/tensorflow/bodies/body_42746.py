# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
variant_t = list_ops.tensor_list_reserve(
    element_shape=[], num_elements=1, element_dtype=dtypes.float32)
with self.assertRaisesRegex(BufferError, "Cannot convert .+ variant"):
    np.asarray(memoryview(variant_t))
