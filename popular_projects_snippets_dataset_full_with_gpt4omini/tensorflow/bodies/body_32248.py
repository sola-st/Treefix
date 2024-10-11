# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings_ja = [
    b"\x5c\x5c",  # Yen sign
    b"\x8f\x70",  # kanji character "waza"
    b"\x83\x4f"
]  # katakana character "gu"
strings_zh_cn = [b"\xca\xf5"]  # simplified "shu4"
strings_zh_tw = [b"\xb3\x4e"]  # traditional "shu4"
strings_ko = [b"\xc7\xd1\xb9\xce"]  # hangul "hanmin"

expected_ja = [s.decode("shift_jis").encode("UTF-8") for s in strings_ja]
expected_zh_cn = [
    s.decode("gb18030").encode("UTF-8") for s in strings_zh_cn
]
expected_zh_tw = [s.decode("big5").encode("UTF-8") for s in strings_zh_tw]
expected_ko = [s.decode("euc_kr").encode("UTF-8") for s in strings_ko]

with self.cached_session() as sess:
    outputs_ja = string_ops.unicode_transcode(
        strings_ja,
        input_encoding="shift_jis",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)

    outputs_zh_cn = string_ops.unicode_transcode(
        strings_zh_cn,
        input_encoding="gb18030",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)

    outputs_zh_tw = string_ops.unicode_transcode(
        strings_zh_tw,
        input_encoding="big5",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)

    outputs_ko = string_ops.unicode_transcode(
        strings_ko,
        input_encoding="euc_kr",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)

    result_ja, result_zh_cn, result_zh_tw, result_ko = sess.run(
        [outputs_ja, outputs_zh_cn, outputs_zh_tw, outputs_ko])

    self.assertAllEqual(result_ja, expected_ja)
    self.assertAllEqual(result_zh_cn, expected_zh_cn)
    self.assertAllEqual(result_zh_tw, expected_zh_tw)
    self.assertAllEqual(result_ko, expected_ko)
