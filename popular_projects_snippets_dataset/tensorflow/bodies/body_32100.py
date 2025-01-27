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

test_string_tensor = np.array(test_string)
for _ in range(rank - 1):
    test_string_tensor = np.expand_dims(test_string_tensor, axis=0)

with self.assertRaises(errors_impl.UnimplementedError):
    # substr is only supported up to rank 2
    substr_op = string_ops.substr(
        test_string_tensor, position, length, unit=unit)
    self.evaluate(substr_op)
