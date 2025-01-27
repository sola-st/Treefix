# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_strip_op_test.py
strings = [["pigs on the wing", "animals"],
           [" hello ", "\n\tworld \r \n"]]

with self.cached_session() as sess:
    output = string_ops.string_strip(strings)
    output = self.evaluate(output)
    self.assertAllEqual(output, [[b"pigs on the wing", b"animals"],
                                 [b"hello", b"world"]])
