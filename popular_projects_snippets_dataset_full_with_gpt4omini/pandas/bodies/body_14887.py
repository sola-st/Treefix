# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series([1, 2, 3, 4])
ax = s.plot.bar(color=["red", "blue", "blue", "red"])
result = [p.get_facecolor() for p in ax.patches]
expected = [
    (1.0, 0.0, 0.0, 1.0),
    (0.0, 0.0, 1.0, 1.0),
    (0.0, 0.0, 1.0, 1.0),
    (1.0, 0.0, 0.0, 1.0),
]
assert result == expected
