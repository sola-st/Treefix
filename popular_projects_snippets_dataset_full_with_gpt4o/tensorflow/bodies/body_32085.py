# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Empty string
test_string = {
    "BYTE": b"",
    "UTF8_CHAR": u"".encode("utf-8"),
}[unit]
expected_value = b""
position = np.array(0, dtype)
length = np.array(3, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)

# Full string
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"H\xc3ll\U0001f604".encode("utf-8"),
}[unit]
position = np.array(0, dtype)
length = np.array(5, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, test_string)

# Full string (Negative)
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"H\xc3ll\U0001f604".encode("utf-8"),
}[unit]
position = np.array(-5, dtype)
length = np.array(5, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, test_string)

# Length is larger in magnitude than a negative position
test_string = {
    "BYTE": b"Hello",
    "UTF8_CHAR": u"H\xc3ll\U0001f604".encode("utf-8"),
}[unit]
expected_string = {
    "BYTE": b"ello",
    "UTF8_CHAR": u"\xc3ll\U0001f604".encode("utf-8"),
}[unit]
position = np.array(-4, dtype)
length = np.array(5, dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_string)
