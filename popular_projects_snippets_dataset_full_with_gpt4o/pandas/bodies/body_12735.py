# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
class _TestObject:
    def __init__(self, a, b, _c, d) -> None:
        self.a = a
        self.b = b
        self._c = _c
        self.d = d

    def e(self):
        exit(5)

        # JSON keys should be all non-callable non-underscore attributes, see GH-42768
test_object = _TestObject(a=1, b=2, _c=3, d=4)
assert ujson.decode(ujson.encode(test_object)) == {"a": 1, "b": 2, "d": 4}
