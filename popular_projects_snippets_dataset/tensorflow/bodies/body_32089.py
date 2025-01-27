# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
# Broadcast pos/len onto input string
test_string = {
    "BYTE": [[b"ten", b"eleven", b"twelve"],
             [b"thirteen", b"fourteen", b"fifteen"],
             [b"sixteen", b"seventeen", b"eighteen"],
             [b"nineteen", b"twenty", b"twentyone"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d229\U0001d227n",
                                               u"\xc6\u053c\u025bv\u025bn",
                                               u"tw\u0c1dlv\u025b"]],
                  [x.encode("utf-8") for x in [u"th\xcdrt\xea\xean",
                                               u"f\U0001f604urt\xea\xean",
                                               u"f\xcd\ua09ctee\ua0e4"]],
                  [x.encode("utf-8") for x in [u"s\xcdxt\xea\xean",
                                               u"se\U00010299enteen",
                                               u"ei\U0001e920h\x86een"]],
                  [x.encode("utf-8") for x in [u"nineteen",
                                               u"twenty",
                                               u"twentyone"]]],
}[unit]
position = np.array([1, -4, 3], dtype)
length = np.array([1, 2, 3], dtype)
expected_value = {
    "BYTE": [[b"e", b"ev", b"lve"], [b"h", b"te", b"tee"],
             [b"i", b"te", b"hte"], [b"i", b"en", b"nty"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d227",
                                               u"\u025bv", u"lv\u025b"]],
                  [x.encode("utf-8") for x in [u"h", u"t\xea", u"tee"]],
                  [x.encode("utf-8") for x in [u"\xcd", u"te", u"h\x86e"]],
                  [x.encode("utf-8") for x in [u"i", u"en", u"nty"]]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)

# Broadcast input string onto pos/len
test_string = {
    "BYTE": [b"thirteen", b"fourteen", b"fifteen"],
    "UTF8_CHAR": [x.encode("utf-8") for x in [u"th\xcdrt\xea\xean",
                                              u"f\U0001f604urt\xea\xean",
                                              u"f\xcd\ua09ctee\ua0e4"]],
}[unit]
position = np.array([[1, -2, 3], [-3, 2, 1], [5, 5, -5]], dtype)
length = np.array([[3, 2, 1], [1, 2, 3], [2, 2, 2]], dtype)
expected_value = {
    "BYTE": [[b"hir", b"en", b"t"], [b"e", b"ur", b"ift"],
             [b"ee", b"ee", b"ft"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"h\xcdr", u"\xean", u"t"]],
                  [x.encode("utf-8") for x in [u"\xea", u"ur",
                                               u"\xcd\ua09ct"]],
                  [x.encode("utf-8") for x in [u"\xea\xea", u"\xea\xea",
                                               u"\ua09ct"]]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)

# Test 1D broadcast
test_string = {
    "BYTE": b"thirteen",
    "UTF8_CHAR": u"th\xcdrt\xea\xean".encode("utf-8"),
}[unit]
position = np.array([1, -4, 7], dtype)
length = np.array([3, 2, 1], dtype)
expected_value = {
    "BYTE": [b"hir", b"te", b"n"],
    "UTF8_CHAR": [x.encode("utf-8") for x in [u"h\xcdr", u"t\xea", u"n"]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)
