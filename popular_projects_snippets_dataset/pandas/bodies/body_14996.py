# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH39126
# Test barh plot with string and integer at the same column
from matplotlib.text import Text

df = DataFrame([{"word": 1, "value": 0}, {"word": "knowledg", "value": 2}])
plot_barh = df.plot.barh(x="word", legend=None)
expected_yticklabels = [Text(0, 0, "1"), Text(0, 1, "knowledg")]
assert all(
    actual.get_text() == expected.get_text()
    for actual, expected in zip(
        plot_barh.get_yticklabels(), expected_yticklabels
    )
)
