# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_upper_op_test.py
strings = [["óósschloë"]]
with self.cached_session():
    output = string_ops.string_upper(strings, encoding="utf-8")
    output = self.evaluate(output)
    # output: "ÓÓSSCHLOË"
    self.assertAllEqual(output, [[b"\xc3\x93\xc3\x93SSCHLO\xc3\x8b"]])
