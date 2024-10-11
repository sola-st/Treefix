# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_raw_op_test.py
self.assertAllEqual(
    [[0x04030201]],
    parsing_ops.decode_raw(
        ["\x01\x02\x03\x04"], dtypes.int32, little_endian=True))
self.assertAllEqual(
    [[0x01020304]],
    parsing_ops.decode_raw(
        ["\x01\x02\x03\x04"], dtypes.int32, little_endian=False))
self.assertAllEqual([[1 + 2j]],
                    parsing_ops.decode_raw([b"\x00\x00\x80?\x00\x00\x00@"],
                                           dtypes.complex64,
                                           little_endian=True))
self.assertAllEqual([[1 + 2j]],
                    parsing_ops.decode_raw([b"?\x80\x00\x00@\x00\x00\x00"],
                                           dtypes.complex64,
                                           little_endian=False))
