# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_format_op_test.py
with self.cached_session():
    tensor = constant_op.constant("😊")
    format_output = string_ops.string_format("😊:{}", tensor)
    out = self.evaluate(format_output)
    expected = '😊:"😊"'
    self.assertEqual(compat.as_text(out), expected)
