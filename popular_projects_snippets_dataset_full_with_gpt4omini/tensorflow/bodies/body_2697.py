# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if dtype == np.float64 and self.backend.platform == "tpu":
    self.skipTest("TPU doesn't support float64")
input_array = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=dtype)
c = self._NewComputation()
window_dimensions = (2, 1)
window_strides = (1, 2)
padding = xla_client.window_padding_type_to_pad_values(
    xla_client.PaddingType.VALID, input_array.shape, window_dimensions,
    window_strides)
ops.ReduceWindowWithGeneralPadding(
    operand=ops.Constant(c, input_array),
    init_value=ops.Constant(c, dtype(0)),
    computation=self._CreateBinaryAddComputation(dtype),
    window_dimensions=window_dimensions,
    window_strides=window_strides,
    base_dilations=[],
    window_dilations=[],
    padding=padding)
self._ExecuteAndCompareClose(c, expected=[[[5., 9.]]])
