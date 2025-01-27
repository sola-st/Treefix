# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
test_string = {
    "BYTE": [b"Hello", b"World"],
    "UTF8_CHAR": [x.encode("utf-8") for x in [u"H\xc3llo",
                                              u"W\U0001f604rld"]],
}[unit]
expected_value = {
    "BYTE": [b"ell", b"orl"],
    "UTF8_CHAR": [x.encode("utf-8") for x in [u"\xc3ll", u"\U0001f604rl"]],
}[unit]
position = np.array(pos, dtype)
length = np.array(3, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)
