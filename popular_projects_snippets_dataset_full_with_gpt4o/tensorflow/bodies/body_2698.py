# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation("reducer")
shape = xla_client.shape_from_pyval(np.array(0, dtype=np.int32))
shape = shape.with_major_to_minor_layout_if_absent()
ps = [ops.Parameter(c, i, shape) for i in range(4)]
which = ops.Ge(ps[0], ps[2])
ops.Tuple(
    c, [ops.Select(which, ps[0], ps[2]),
        ops.Select(which, ps[1], ps[3])])
reducer = c.build()

key_array = np.array([[1, 5, 6], [4, 2, 3]], dtype=np.int32)
val_array = np.array([[7, 8, 9], [10, 11, 12]], dtype=np.int32)
c = self._NewComputation()
window_dimensions = (2, 1)
window_strides = (1, 1)
padding = xla_client.window_padding_type_to_pad_values(
    xla_client.PaddingType.VALID, key_array.shape, window_dimensions,
    window_strides)
ops.ReduceWindowWithGeneralPadding(
    operands=[ops.Constant(c, key_array),
              ops.Constant(c, val_array)],
    init_values=[
        ops.Constant(c, np.int32(0)),
        ops.Constant(c, np.int32(0))
    ],
    computation=reducer,
    window_dimensions=window_dimensions,
    window_strides=window_strides,
    base_dilations=[],
    window_dilations=[],
    padding=padding)
self._ExecuteAndCompareClose(c, expected=[[[4, 5, 6]], [[10, 8, 9]]])
