# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Matrix/Matrix
test_string = {
    "BYTE": [[b"good", b"good", b"good"], [b"good", b"good", b"bad"],
             [b"good", b"good", b"good"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"g\xc3\xc3d", u"g\xc3\xc3d",
                                               u"g\xc3\xc3d"]],
                  [x.encode("utf-8") for x in [u"g\xc3\xc3d", u"g\xc3\xc3d",
                                               u"b\xc3d"]],
                  [x.encode("utf-8") for x in [u"g\xc3\xc3d", u"g\xc3\xc3d",
                                               u"g\xc3\xc3d"]]],
}[unit]
position = np.array([[1, 2, 3], [1, 2, 4], [1, 2, 3]], dtype)
length = np.array([[3, 2, 1], [1, 2, 3], [2, 2, 2]], dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    with self.assertRaises(errors_impl.InvalidArgumentError):
        self.evaluate(substr_op)

    # Matrix/Matrix (with negative)
position = np.array([[1, 2, -3], [1, 2, -4], [1, 2, -3]], dtype)
length = np.array([[3, 2, 1], [1, 2, 3], [2, 2, 2]], dtype)
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    with self.assertRaises(errors_impl.InvalidArgumentError):
        self.evaluate(substr_op)
