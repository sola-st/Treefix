# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_length_op_test.py
unicode_strings = [u"H\xc3llo", u"\U0001f604"]
utf8_strings = [s.encode("utf-8") for s in unicode_strings]
expected_utf8_byte_lengths = [6, 4]
expected_utf8_char_lengths = [5, 1]

with self.session() as sess:
    utf8_byte_lengths = string_ops.string_length(utf8_strings, unit="BYTE")
    utf8_char_lengths = string_ops.string_length(
        utf8_strings, unit="UTF8_CHAR")
    self.assertAllEqual(
        self.evaluate(utf8_byte_lengths), expected_utf8_byte_lengths)
    self.assertAllEqual(
        self.evaluate(utf8_char_lengths), expected_utf8_char_lengths)
    with self.assertRaisesRegex(
        ValueError, "Attr 'unit' of 'StringLength' Op passed string 'XYZ' "
        'not in: "BYTE", "UTF8_CHAR"'):
        string_ops.string_length(utf8_strings, unit="XYZ")
