# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
class _TestObject:
    def __init__(self, a, b, _c, d) -> None:
        self.a = a
        self.b = b
        self._c = _c
        self.d = d

    def e(self):
        exit(5)

        # JSON keys should be all non-callable non-underscore attributes, see GH-42768
series = Series([_TestObject(a=1, b=2, _c=3, d=4)])
assert json.loads(series.to_json()) == {"0": {"a": 1, "b": 2, "d": 4}}
