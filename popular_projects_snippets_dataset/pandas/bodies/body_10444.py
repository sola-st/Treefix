# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH#49834 - as_index should have no impact on DataFrameGroupBy.transform
if keys == "A":
    # Column B is string dtype; will fail on some ops
    df = df.drop(columns="B")
args = get_groupby_method_args(groupby_func, df)
gb_as_index_true = df.groupby(keys, as_index=True)
gb_as_index_false = df.groupby(keys, as_index=False)
result = gb_as_index_true.transform(groupby_func, *args)
expected = gb_as_index_false.transform(groupby_func, *args)
tm.assert_equal(result, expected)
