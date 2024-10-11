# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame(
    {"A": range(4), "B": range(1, 5), "color": ["red", "blue", "blue", "red"]}
)
# This should *only* work when `y` is specified, else
# we use one color per column
ax = df.plot.bar(y="A", color=df["color"])
result = [p.get_facecolor() for p in ax.patches]
expected = [
    (1.0, 0.0, 0.0, 1.0),
    (0.0, 0.0, 1.0, 1.0),
    (0.0, 0.0, 1.0, 1.0),
    (1.0, 0.0, 0.0, 1.0),
]
assert result == expected
