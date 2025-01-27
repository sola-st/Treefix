# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if dtype == np.float64 and self.backend.platform == "tpu":
    self.skipTest("TPU doesn't support float64")
c = self._NewComputation()
operand = ops.Constant(
    c, np.array([[1., 2., 6.], [4., 5., 3.]], dtype=dtype))
window_dimensions = (2, 1)
window_strides = (1, 2)
padding = xla_client.window_padding_type_to_pad_values(
    xla_client.PaddingType.VALID,
    c.get_shape(operand).dimensions(), window_dimensions, window_strides)
ops.SelectAndScatterWithGeneralPadding(
    operand,
    select=self._CreateBinaryGeComputation(dtype),
    window_dimensions=window_dimensions,
    window_strides=window_strides,
    padding=padding,
    source=ops.Constant(c, np.array([[0.1, 0.2]], dtype=dtype)),
    init_value=ops.Constant(c, np.array(1, dtype=dtype)),
    scatter=self._CreateBinaryAddComputation(dtype))
self._ExecuteAndCompareClose(
    c, expected=[[[1., 1., 1.2], [1.1, 1., 1.]]], rtol=5e-3)
