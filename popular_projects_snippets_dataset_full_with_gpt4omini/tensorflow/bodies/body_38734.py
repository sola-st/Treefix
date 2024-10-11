# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_bmp_op_test.py
img_bytes = [[[0, 0, 255], [0, 255, 0]], [[255, 0, 0], [255, 255, 255]]]
# Encoded BMP bytes from Wikipedia
# BMP header bytes: https://en.wikipedia.org/wiki/List_of_file_signatures
encoded_bytes = [
    0x42, 0x4d,
    0x46, 0, 0, 0,
    0, 0,
    0, 0,
    0x36, 0, 0, 0,
    0x28, 0, 0, 0,
    0x2, 0, 0, 0,
    0x2, 0, 0, 0,
    0x1, 0,
    0x18, 0,
    0, 0, 0, 0,
    0x10, 0, 0, 0,
    0x13, 0xb, 0, 0,
    0x13, 0xb, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0xff,
    0xff, 0xff, 0xff,
    0, 0,
    0xff, 0, 0,
    0, 0xff, 0,
    0, 0,
]

byte_string = bytes(bytearray(encoded_bytes))
img_in = constant_op.constant(byte_string, dtype=dtypes.string)
decode = array_ops.squeeze(image_ops.decode_bmp(img_in))

with self.cached_session():
    decoded = self.evaluate(decode)
    self.assertAllEqual(decoded, img_bytes)
