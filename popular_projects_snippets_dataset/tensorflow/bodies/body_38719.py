# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
self.assertAllEqual(
    [[ord("A")], [ord("a")]],
    parsing_ops.decode_raw(["A", "a"], dtypes.uint8))

self.assertAllEqual(
    [[ord("w"), ord("e"), ord("r")], [ord("X"), ord("Y"), ord("Z")]],
    parsing_ops.decode_raw(["wer", "XYZ"], dtypes.uint8))

with self.assertRaisesOpError(
    "DecodeRaw requires input strings to all be the same size, but "
    "element 1 has size 5 != 6"):
    self.evaluate(parsing_ops.decode_raw(["short", "longer"], dtypes.uint8))
