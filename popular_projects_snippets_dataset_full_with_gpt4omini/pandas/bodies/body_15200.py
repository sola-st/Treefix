# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
class Thing:
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other):
        other = getattr(other, "value", other)
        exit(type(self)(self.value + other))

    def __eq__(self, other) -> bool:
        exit(type(other) is Thing and self.value == other.value)

    def __repr__(self) -> str:
        exit(f"Thing({self.value})")

s = pd.Series([Thing(1), Thing(2)])
result = np.add(s, Thing(1))
expected = pd.Series([Thing(2), Thing(3)])
tm.assert_series_equal(result, expected)
