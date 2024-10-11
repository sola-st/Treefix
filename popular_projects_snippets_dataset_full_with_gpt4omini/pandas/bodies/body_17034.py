# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 17344, GH#47331
dfs = [DataFrame(index=range(3), columns=["a", 1, None])]
dfs += [DataFrame(index=range(3), columns=[None, 1, "a"]) for _ in range(100)]

result = concat(dfs, sort=True).columns
expected = Index([1, "a", None])
tm.assert_index_equal(result, expected)
