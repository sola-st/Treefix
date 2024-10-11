# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [[b"a", b"abc"], [b"ABC", b"DEF"]]

with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="UTF-8",
        output_encoding="UTF-8",
        errors="replace",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, strings)

    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="ISO-8859-1",
        output_encoding="UTF-8",
        errors="replace",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, strings)

    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="US-ASCII",
        output_encoding="UTF-8",
        errors="replace",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, strings)
