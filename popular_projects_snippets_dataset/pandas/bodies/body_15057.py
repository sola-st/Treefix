# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
# GH10214
bins = np.arange(80, 100 + 2, 1)
df = DataFrame({"Name": ["AAA", "BBB"], "ByCol": [1, 2], "Mark": [85, 89]})
df["Mark"].hist(by=df["ByCol"], bins=bins)
df = DataFrame({"Name": ["AAA"], "ByCol": [1], "Mark": [85]})
df["Mark"].hist(by=df["ByCol"], bins=bins)
