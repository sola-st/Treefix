# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_image_op_test.py
image_bytes = b"ThisIsNotAnImage!"
decode = image_ops.decode_image(image_bytes)
with self.cached_session():
    with self.assertRaises(errors_impl.InvalidArgumentError):
        self.evaluate(decode)
