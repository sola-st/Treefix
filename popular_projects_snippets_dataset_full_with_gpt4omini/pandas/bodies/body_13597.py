# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
df = DataFrame([[1, 2, 3, 4]])
df.columns = MultiIndex.from_tuples([("A", 1), ("A", 2), ("A", 3), ("B", 1)])
s = df.style
assert "{tabular}{lrrrr}" in s.to_latex()
s.set_table_styles([])  # reset the position command
s.hide([("A", 2)], axis="columns")
assert "{tabular}{lrrr}" in s.to_latex()
