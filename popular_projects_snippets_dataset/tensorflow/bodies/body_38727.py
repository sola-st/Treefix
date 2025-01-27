# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
# Use FF/EE/DD/CC so that decoded value is higher than 32768 for uint16
self.assertAllEqual(
    [[0xFF + 0xEE * 256, 0xDD + 0xCC * 256]],
    parsing_ops.decode_raw([b"\xFF\xEE\xDD\xCC"], dtypes.uint16))

with self.assertRaisesOpError(
    "Input to DecodeRaw has length 3 that is not a multiple of 2, the "
    "size of uint16"):
    self.evaluate(parsing_ops.decode_raw(["123", "456"], dtypes.uint16))
