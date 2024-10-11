# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
lst = [["count", "values"], ["to filter", ""]]
midx = MultiIndex.from_tuples(lst)

df = DataFrame([[1, "A"]], columns=midx)

grouped = df.groupby("to filter").groups
assert grouped["A"] == [0]

grouped = df.groupby([("to filter", "")]).groups
assert grouped["A"] == [0]

df = DataFrame([[1, "A"], [2, "B"]], columns=midx)

expected = df.groupby("to filter").groups
result = df.groupby([("to filter", "")]).groups
assert result == expected

df = DataFrame([[1, "A"], [2, "A"]], columns=midx)

expected = df.groupby("to filter").groups
result = df.groupby([("to filter", "")]).groups
tm.assert_dict_equal(result, expected)
