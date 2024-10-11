# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"A": [10, np.nan, 20], "B": [5, 10, 20], "C": [1, 2, 3]})
ax = df.plot.bar()
expected = [10, 0, 20, 5, 10, 20, 1, 2, 3]
result = [p.get_height() for p in ax.patches]
assert result == expected

ax = df.plot.bar(stacked=True)
result = [p.get_height() for p in ax.patches]
assert result == expected

result = [p.get_y() for p in ax.patches]
expected = [0.0, 0.0, 0.0, 10.0, 0.0, 20.0, 15.0, 10.0, 40.0]
assert result == expected
