# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [b"a\xef\xbf\xbd"]
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings, input_encoding="UTF-8", output_encoding="UTF-8",
        errors="strict")
    values = self.evaluate(outputs)
    self.assertAllEqual(values, [b"a\xef\xbf\xbd"])

    outputs = string_ops.unicode_transcode(
        strings, input_encoding="UTF-8", output_encoding="UTF-8",
        errors="replace", replacement_char=ord("?"))
    values = self.evaluate(outputs)
    self.assertAllEqual(values, [b"a\xef\xbf\xbd"])
