# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
a = lambda *dims: np.arange(np.prod(dims)).reshape(dims).astype("float32")
lhs = a(1, 1, 2, 3)
rhs = a(1, 1, 1, 2) * 10
strides = [1, 1]
pads = [(1, 0), (0, 1)]
lhs_dilation = (2, 1)
rhs_dilation = (1, 1)
window_reversal = [False, True]
dimension_numbers = xla_client.make_convolution_dimension_numbers(
    ("NCHW", "OIHW", "NCHW"), 2)
ops.ConvGeneralDilated(
    ops.Constant(c, lhs),
    ops.Constant(c, rhs),
    strides,
    pads,
    lhs_dilation,
    rhs_dilation,
    dimension_numbers,
    window_reversal=window_reversal)
result = np.array([[[
    [0., 0., 0.],
    [0., 10., 20.],
    [0., 0., 0.],
    [30., 40., 50.],
]]])
self._ExecuteAndCompareClose(c, expected=[result])
