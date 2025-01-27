# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 13394
mi = MultiIndex.from_arrays([list("AAB"), list("aba")])
df = DataFrame([[1, 2, 3]], columns=mi)
gr = df.groupby(df[("A", "a")])

result = gr.grouper.groupings[0].__repr__()
expected = "Grouping(('A', 'a'))"
assert result == expected
