# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    format_output = string_ops.string_format("No tensor.", ())
    out = self.evaluate(format_output)
    expected = "No tensor."
    self.assertEqual(compat.as_text(out), expected)
