# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"A": ["x", "y", "z"], "B": [1, 2, 3]})
ax = df.plot()
assert len(ax.get_lines()) == 1  # B was plotted
