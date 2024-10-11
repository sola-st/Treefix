# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
result = np.matrix([[1, -2, -3, 4]], dtype="<f2")
self.assertAllEqual(
    result, parsing_ops.decode_raw([result.tobytes()], dtypes.float16))
