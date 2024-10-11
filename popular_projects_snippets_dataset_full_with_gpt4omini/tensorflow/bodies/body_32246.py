# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [[b"a", b"abc"], [b"ABC", b"DEF"]]

with self.assertRaisesRegex(
    ValueError, "'invalid' not in: \"strict\", \"replace\", \"ignore\"."):
    with self.cached_session() as sess:
        outputs = string_ops.unicode_transcode(
            strings,
            input_encoding="UTF-8",
            output_encoding="UTF-8",
            errors="invalid",
            replacement_char=ord(" "),
            replace_control_characters=False)
        self.evaluate(outputs)
