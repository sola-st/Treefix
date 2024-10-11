# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    for dtype in [dtypes.bool, dtypes.int8, dtypes.uint8, dtypes.int16,
                  dtypes.uint16, dtypes.int32, dtypes.int64, dtypes.float16,
                  dtypes.float32, dtypes.float64, dtypes.complex64,
                  dtypes.complex128]:
        in_bytes = array_ops.placeholder(dtypes.string, shape=[None])
        decode = parsing_ops.decode_raw(in_bytes, dtype)
        self.assertEqual([None, None], decode.get_shape().as_list())
