# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
if groupby_func in {"size", "ngroup", "cumcount"}:
    pytest.skip(f"Not applicable for {groupby_func}")

df = DataFrame([[1, 1]], columns=idx)
grp_by = df.groupby([0])

args = get_groupby_method_args(groupby_func, df)
result = getattr(grp_by, groupby_func)(*args)

assert result.shape == (1, 2)
tm.assert_index_equal(result.columns, idx)
