# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/substr_op_test.py
test_string = {
    "BYTE": [[b"ten", b"eleven", b"twelve"],
             [b"thirteen", b"fourteen", b"fifteen"],
             [b"sixteen", b"seventeen", b"eighteen"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d229\U0001d227n",
                                               u"\xc6\u053c\u025bv\u025bn",
                                               u"tw\u0c1dlv\u025b"]],
                  [x.encode("utf-8") for x in [u"He\xc3\xc3o",
                                               u"W\U0001f604rld",
                                               u"d\xfcd\xea"]],
                  [x.encode("utf-8") for x in [u"sixt\xea\xean",
                                               u"se\U00010299enteen",
                                               u"ei\U0001e920h\x86een"]]],
}[unit]
position = np.array([[1, -4, 3], [1, 2, -4], [-5, 2, 3]], dtype)
length = np.array([[2, 2, 4], [4, 3, 2], [5, 5, 5]], dtype)
expected_value = {
    "BYTE": [[b"en", b"ev", b"lve"], [b"hirt", b"urt", b"te"],
             [b"xteen", b"vente", b"hteen"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d227n",
                                               u"\u025bv",
                                               u"lv\u025b"]],
                  [x.encode("utf-8") for x in [u"e\xc3\xc3o",
                                               u"rld",
                                               u"d\xfc"]],
                  [x.encode("utf-8") for x in [u"xt\xea\xean",
                                               u"\U00010299ente",
                                               u"h\x86een"]]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)
