# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 11670
# possible bug when calculating mean of DataFrame?

d = [
    {"A": 2, "B": None, "C": Decimal("628.00")},
    {"A": 1, "B": None, "C": Decimal("383.00")},
    {"A": 3, "B": None, "C": Decimal("651.00")},
    {"A": 2, "B": None, "C": Decimal("575.00")},
    {"A": 4, "B": None, "C": Decimal("1114.00")},
    {"A": 1, "B": "TEST", "C": Decimal("241.00")},
    {"A": 2, "B": None, "C": Decimal("572.00")},
    {"A": 4, "B": None, "C": Decimal("609.00")},
    {"A": 3, "B": None, "C": Decimal("820.00")},
    {"A": 5, "B": None, "C": Decimal("1223.00")},
]

df = DataFrame(d)

with pytest.raises(TypeError, match="unsupported operand type"):
    df.mean()
result = df[["A", "C"]].mean()
expected = Series([2.7, 681.6], index=["A", "C"])
tm.assert_series_equal(result, expected)
