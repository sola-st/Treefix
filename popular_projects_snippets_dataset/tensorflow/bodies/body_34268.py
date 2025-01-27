# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
for dtype in (dtypes.uint8, dtypes.uint16, dtypes.int8, dtypes.int16,
              dtypes.int32, dtypes.int64, dtypes.float16, dtypes.float32,
              dtypes.float64, dtypes.complex64, dtypes.complex128,
              dtypes.bool):
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.variant, element_shape=[])

    sub_l = list_ops.empty_tensor_list(element_dtype=dtype, element_shape=[])
    l = list_ops.tensor_list_push_back(l, sub_l)
    sub_l = list_ops.tensor_list_push_back(sub_l, math_ops.cast(
        1, dtype=dtype))
    l = list_ops.tensor_list_push_back(l, sub_l)
    sub_l = list_ops.tensor_list_push_back(sub_l, math_ops.cast(
        2, dtype=dtype))
    l = list_ops.tensor_list_push_back(l, sub_l)

    # l : [[],
    #      [1],
    #      [1, 2]]
    #
    # l_zeros : [[],
    #            [0],
    #            [0, 0]]
    l_zeros = array_ops.zeros_like(l)

    outputs = []
    for _ in range(3):
        l_zeros, out = list_ops.tensor_list_pop_back(
            l_zeros, element_dtype=dtypes.variant)
        outputs.append(list_ops.tensor_list_stack(out, element_dtype=dtype))

    # Note: `outputs` contains popped values so the order is reversed.
    self.assertAllEqual(self.evaluate(outputs[2]), [])
    self.assertAllEqual(
        self.evaluate(outputs[1]), np.zeros((1,), dtype=dtype.as_numpy_dtype))
    self.assertAllEqual(
        self.evaluate(outputs[0]), np.zeros((2,), dtype=dtype.as_numpy_dtype))
