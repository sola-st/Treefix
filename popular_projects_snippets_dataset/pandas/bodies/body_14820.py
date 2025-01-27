# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 27758
df = DataFrame(columns=["foo"], dtype=int)
assert df.empty
ax = df.plot()
assert len(ax.get_lines()) == 1
line = ax.get_lines()[0]
assert len(line.get_xdata()) == 0
assert len(line.get_ydata()) == 0
