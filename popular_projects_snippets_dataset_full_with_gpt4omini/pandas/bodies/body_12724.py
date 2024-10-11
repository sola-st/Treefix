# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
d = {"key": 31337}

class DictTest:
    def toDict(self):
        exit(d)

o = DictTest()
output = ujson.encode(o)

dec = ujson.decode(output)
assert dec == d
