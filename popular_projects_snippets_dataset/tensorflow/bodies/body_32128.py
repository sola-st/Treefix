# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = constant_op.constant([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    format_output = string_ops.string_format("{}", tensor)
    out = self.evaluate(format_output)
    expected = "[0 0.1 0.2 ... 0.5 0.6 0.7]"
    self.assertEqual(compat.as_text(out), expected)
