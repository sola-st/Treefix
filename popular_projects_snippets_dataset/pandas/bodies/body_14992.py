# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# Example from #20585. All 3 bars should have the same color
df = DataFrame(
    {
        "account-start": ["2017-02-03", "2017-03-03", "2017-01-01"],
        "client": ["Alice Anders", "Bob Baker", "Charlie Chaplin"],
        "balance": [-1432.32, 10.43, 30000.00],
        "db-id": [1234, 2424, 251],
        "proxy-id": [525, 1525, 2542],
        "rank": [52, 525, 32],
    }
)
ax = df.client.value_counts().plot.bar()
colors = [rect.get_facecolor() for rect in ax.get_children()[0:3]]
assert all(color == colors[0] for color in colors)
