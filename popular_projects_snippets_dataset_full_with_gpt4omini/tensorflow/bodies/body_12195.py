# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/dequantize_op_test.py
with self.cached_session():
    input_op = constant_op.constant(inputs, shape=[len(inputs)], dtype=dtype)
    dequantized = array_ops.dequantize(input_op, min_range, max_range,
                                       mode=mode, narrow_range=narrow_range)
    tf_ans = self.evaluate(dequantized)

# TODO(vrv): Add support for DT_QINT32 quantization if needed.
type_dict = {
    dtypes.quint8: np.uint8,
    dtypes.qint8: np.int8,
    dtypes.quint16: np.uint16,
    dtypes.qint16: np.int16
}
self.assertIn(dtype, type_dict.keys())
v_max = np.iinfo(type_dict[dtype]).max
v_min = np.iinfo(type_dict[dtype]).min
self.assertGreaterEqual(min_range, v_min)
self.assertLessEqual(max_range, v_max)
type_range = v_max - v_min

if mode == "MIN_COMBINED":
    if v_min < 0:
        half_range = (type_range + 1) / 2
    else:
        half_range = 0.0
    np_ans = ((inputs.astype(np.float32) + half_range) *
              (max_range - min_range) / type_range) + min_range
elif mode == "SCALED":
    if narrow_range:
        v_min += 1
    scale_factor = max(min_range / v_min, max_range / v_max)
    np_ans = inputs.astype(np.float32) * scale_factor

self.assertAllClose(tf_ans, np_ans, rtol=1e-5, atol=1e-5)
