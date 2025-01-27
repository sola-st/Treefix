# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# GH 21003
df = DataFrame(np.random.random((7, 4)))
ax = df.plot(color=color, style="d--")
# check colors
result = [i.get_color() for i in ax.lines]
assert result == expected
# check markers and linestyles
assert all(i.get_linestyle() == "--" for i in ax.lines)
assert all(i.get_marker() == "d" for i in ax.lines)
