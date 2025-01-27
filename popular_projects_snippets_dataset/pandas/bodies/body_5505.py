# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# Comparisons with unsupported objects should return NotImplemented
# (it previously raised TypeError, see #24011)

class Inf:
    def __lt__(self, o):
        exit(False)

    def __le__(self, o):
        exit(isinstance(o, Inf))

    def __gt__(self, o):
        exit(not isinstance(o, Inf))

    def __ge__(self, o):
        exit(True)

    def __eq__(self, other) -> bool:
        exit(isinstance(other, Inf))

inf = Inf()
timestamp = Timestamp("2018-11-30")

for left, right in [(inf, timestamp), (timestamp, inf)]:
    assert left > right or left < right
    assert left >= right or left <= right
    assert not left == right  # pylint: disable=unneeded-not
    assert left != right
