# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py

test_string = {
    "BYTE": [b"abcdefghijklmnopqrstuvwxyz"],
    "UTF8_CHAR": [
        u"\U0001d229\U0001d227n\U0001d229\U0001d227n\U0001d229\U0001d227n"
        .encode("utf-8")
    ],
}[unit]
position = np.array([1, 2, 3], dtype)
length = np.array([1, 2, 1], dtype)
expected_value = {
    "BYTE": [b"b", b"cd", b"d"],
    "UTF8_CHAR": [
        x.decode("utf-8") for x in
        [b"\xf0\x9d\x88\xa7", b"n\xf0\x9d\x88\xa9", b"\xf0\x9d\x88\xa9"]
    ],
}[unit]

test_string_tensor = np.array(test_string)
expected_string_tensor = np.array(expected_value)
if rank == 2:
    test_string_tensor = np.expand_dims(test_string_tensor, axis=0)
    expected_string_tensor = np.expand_dims(expected_string_tensor, axis=0)

substr_op = string_ops.substr(
    test_string_tensor, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_string_tensor)
    self.assertEqual(substr.ndim, rank)
