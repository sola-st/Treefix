# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
result = np.matrix([[1 + 1j, 2 - 2j, -3 + 3j, -4 - 4j]], dtype="<c16")
self.assertAllEqual(
    result, parsing_ops.decode_raw([result.tobytes()], dtypes.complex128))
