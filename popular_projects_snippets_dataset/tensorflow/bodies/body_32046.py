# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
with self.cached_session():
    with self.assertRaises(TypeError):
        ragged_string_ops.unicode_encode()  # pylint: disable=no-value-for-parameter
with self.cached_session():
    with self.assertRaises(TypeError):
        ragged_string_ops.unicode_encode(72)  # pylint: disable=no-value-for-parameter
with self.cached_session():
    with self.assertRaises(TypeError):
        ragged_string_ops.unicode_encode(encoding="UTF-8")  # pylint: disable=no-value-for-parameter,unexpected-keyword-arg
