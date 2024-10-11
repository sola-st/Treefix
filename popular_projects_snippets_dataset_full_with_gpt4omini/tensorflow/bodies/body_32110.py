# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_strip_op_test.py
strings = [" hello ", "", "world ", " \t \r \n "]

with self.cached_session() as sess:
    output = string_ops.string_strip(strings)
    output = self.evaluate(output)
    self.assertAllEqual(output, [b"hello", b"", b"world", b""])
