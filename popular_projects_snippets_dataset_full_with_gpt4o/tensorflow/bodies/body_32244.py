# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
with self.test_session():
    output = string_ops.unicode_transcode(
        string, input_encoding=input_encoding, output_encoding="UTF-8")
    self.assertAllEqual(output, expected)
