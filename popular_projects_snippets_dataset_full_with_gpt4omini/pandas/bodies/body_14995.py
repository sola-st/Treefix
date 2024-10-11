# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH38947
# Test bar plot with string and int index
from matplotlib.text import Text

expected = [Text(0, 0, "0"), Text(1, 0, "Total")]

df = DataFrame(
    {
        "a": [1, 2],
    },
    index=Index([0, "Total"]),
)
plot_bar = df.plot.bar()
assert all(
    (a.get_text() == b.get_text())
    for a, b in zip(plot_bar.get_xticklabels(), expected)
)
