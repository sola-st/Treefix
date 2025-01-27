# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 32464
df = DataFrame({"a": [], "b": [], "c": []}).set_index(["a", "b", "c"])
gb = df.groupby(["a", "b", "c"], group_keys=False)
method = getattr(gb, groupby_func)
args = get_groupby_method_args(groupby_func, df)

result = method(*args).index
expected = df.index
tm.assert_index_equal(result, expected)
