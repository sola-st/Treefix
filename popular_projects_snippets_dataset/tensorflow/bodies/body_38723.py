# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
result = np.matrix([[True, False, False, True]], dtype="<b1")
self.assertAllEqual(result,
                    parsing_ops.decode_raw([result.tobytes()], dtypes.bool))
