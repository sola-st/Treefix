# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"He\xc3\xc3\U0001f604".encode("utf-8"),
}[unit]
expected_value = {
    "BYTE": b"ell",
    "UTF8_CHAR": u"e\xc3\xc3".encode("utf-8"),
}[unit]
position = np.array(pos, dtype)
length = np.array(3, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)
