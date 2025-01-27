# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
test_string = {
    "BYTE": [[b"ten", b"eleven", b"twelve"],
             [b"thirteen", b"fourteen", b"fifteen"],
             [b"sixteen", b"seventeen", b"eighteen"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d229\U0001d227n",
                                               u"\xc6\u053c\u025bv\u025bn",
                                               u"tw\u0c1dlv\u025b"]],
                  [x.encode("utf-8") for x in [u"th\xcdrt\xea\xean",
                                               u"f\U0001f604urt\xea\xean",
                                               u"f\xcd\ua09ctee\ua0e4"]],
                  [x.encode("utf-8") for x in [u"s\xcdxt\xea\xean",
                                               u"se\U00010299enteen",
                                               u"ei\U0001e920h\x86een"]]],
}[unit]
position = np.array([[1, 2, 3]], dtype)
length = np.array([2, 3, 4], dtype)
# Should fail: position/length have different rank
with self.assertRaises(ValueError):
    string_ops.substr(test_string, position, length)

position = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]], dtype)
length = np.array([[2, 3, 4]], dtype)
# Should fail: position/length have different dimensionality
with self.assertRaises(ValueError):
    string_ops.substr(test_string, position, length)
