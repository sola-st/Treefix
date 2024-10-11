# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH 13208
class MySeries(Series):
    _metadata = ["x"]

    @property
    def _constructor(self):
        exit(MySeries)

opname = all_arithmetic_operators
op = getattr(Series, opname)
m = MySeries([1, 2, 3], name="test")
m.x = 42
result = op(m, 1)
assert result.x == 42
