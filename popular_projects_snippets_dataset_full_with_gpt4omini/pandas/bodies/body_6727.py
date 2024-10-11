# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_formats.py
# https://github.com/pandas-dev/pandas/pull/24134/files
df = DataFrame(
    {"A": [1, 2, 3, 4]}, index=IntervalIndex.from_breaks([0, 1, 2, 3, 4])
)
result = repr(df)
expected = "        A\n(0, 1]  1\n(1, 2]  2\n(2, 3]  3\n(3, 4]  4"
assert result == expected
