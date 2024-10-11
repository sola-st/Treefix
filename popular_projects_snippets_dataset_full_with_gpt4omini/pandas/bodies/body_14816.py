# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# Test if string plot index have a fixed xtick position
# GH: 7612, GH: 22334
df = DataFrame(
    {
        "sales": [3, 2, 3],
        "visits": [20, 42, 28],
        "day": ["Monday", "Tuesday", "Wednesday"],
    }
)
ax = df.plot.area(x="day")
ax.set_xlim(-1, 3)
xticklabels = [t.get_text() for t in ax.get_xticklabels()]
labels_position = dict(zip(xticklabels, ax.get_xticks()))
# Testing if the label stayed at the right position
assert labels_position["Monday"] == 0.0
assert labels_position["Tuesday"] == 1.0
assert labels_position["Wednesday"] == 2.0
