# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
self.assertAllEqual(
    [[ord("A") + ord("a") * 256, ord("B") + ord("C") * 256]],
    parsing_ops.decode_raw(["AaBC"], dtypes.uint16))

with self.assertRaisesOpError(
    "Input to DecodeRaw has length 3 that is not a multiple of 2, the "
    "size of int16"):
    self.evaluate(parsing_ops.decode_raw(["123", "456"], dtypes.int16))
