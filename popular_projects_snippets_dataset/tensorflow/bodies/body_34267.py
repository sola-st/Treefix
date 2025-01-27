# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
for dtype in (dtypes.uint8, dtypes.uint16, dtypes.int8, dtypes.int16,
              dtypes.int32, dtypes.int64, dtypes.float16, dtypes.float32,
              dtypes.float64, dtypes.complex64, dtypes.complex128,
              dtypes.bool):
    l_empty = list_ops.empty_tensor_list(
        element_dtype=dtype, element_shape=[])
    l_empty_zeros = array_ops.zeros_like(l_empty)
    t_empty_zeros = list_ops.tensor_list_stack(
        l_empty_zeros, element_dtype=dtype)

    l_full = list_ops.tensor_list_push_back(l_empty,
                                            math_ops.cast(0, dtype=dtype))
    l_full = list_ops.tensor_list_push_back(l_full,
                                            math_ops.cast(1, dtype=dtype))
    l_full_zeros = array_ops.zeros_like(l_full)
    t_full_zeros = list_ops.tensor_list_stack(
        l_full_zeros, element_dtype=dtype)

    self.assertAllEqual(self.evaluate(t_empty_zeros), [])
    self.assertAllEqual(
        self.evaluate(t_full_zeros), np.zeros(
            (2,), dtype=dtype.as_numpy_dtype))
