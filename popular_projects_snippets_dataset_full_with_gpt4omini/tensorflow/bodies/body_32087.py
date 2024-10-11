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
                                               u"d\xfcd\xea"]]],
}[unit]
position = np.array(1, dtype)
length = np.array(4, dtype)
expected_value = {
    "BYTE": [[b"en", b"leve", b"welv"], [b"hirt", b"ourt", b"ifte"],
             [b"ixte", b"even", b"ight"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d227n",
                                               u"\u053c\u025bv\u025b",
                                               u"w\u0c1dlv"]],
                  [x.encode("utf-8") for x in [u"e\xc3\xc3o",
                                               u"\U0001f604rld",
                                               u"\xfcd\xea"]]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)

position = np.array(-3, dtype)
length = np.array(2, dtype)
expected_value = {
    "BYTE": [[b"te", b"ve", b"lv"], [b"ee", b"ee", b"ee"],
             [b"ee", b"ee", b"ee"]],
    "UTF8_CHAR": [[x.encode("utf-8") for x in [u"\U0001d229\U0001d227",
                                               u"v\u025b", u"lv"]],
                  [x.encode("utf-8") for x in [u"\xc3\xc3", u"rl",
                                               u"\xfcd"]]],
}[unit]
substr_op = string_ops.substr(test_string, position, length, unit=unit)
with self.cached_session():
    substr = self.evaluate(substr_op)
    self.assertAllEqual(substr, expected_value)
