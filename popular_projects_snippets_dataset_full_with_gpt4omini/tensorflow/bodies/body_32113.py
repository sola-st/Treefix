# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_lower_op_test.py
strings = [["ÓÓSSCHLOË"]]
with self.cached_session():
    output = string_ops.string_lower(strings, encoding="utf-8")
    output = self.evaluate(output)
    # output: "óósschloë"
    self.assertAllEqual(output, [[b"\xc3\xb3\xc3\xb3sschlo\xc3\xab"]])
