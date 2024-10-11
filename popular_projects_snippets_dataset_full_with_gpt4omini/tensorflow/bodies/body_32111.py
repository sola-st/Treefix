# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_lower_op_test.py
strings = ["Pigs on The Wing", "aNimals"]

with self.cached_session():
    output = string_ops.string_lower(strings)
    output = self.evaluate(output)
    self.assertAllEqual(output, [b"pigs on the wing", b"animals"])
