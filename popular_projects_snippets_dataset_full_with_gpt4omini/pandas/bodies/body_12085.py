# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
"""
    read_csv should honor the requested encoding for URLs.

    GH 10424
    """
path = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/"
    + "pandas/tests/io/parser/data/unicode_series.csv"
)
df = read_csv(path, encoding="latin-1", header=None)
assert df.loc[15, 1] == "Á köldum klaka (Cold Fever) (1994)"
