# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH#48749
if (
    reduction_func in ("idxmax", "idxmin")
    and not observed
    and index_kind != "multi"
):
    msg = "GH#10694 - idxmax/min fail with unused categories"
    request.node.add_marker(pytest.mark.xfail(reason=msg))
elif reduction_func == "corrwith" and not as_index:
    msg = "GH#49950 - corrwith with as_index=False may not have grouping column"
    request.node.add_marker(pytest.mark.xfail(reason=msg))
elif index_kind != "range" and not as_index:
    pytest.skip(reason="Result doesn't have categories, nothing to test")
df = DataFrame(
    {
        "a": Categorical([2, 1, 2, 3], categories=[1, 4, 3, 2], ordered=ordered),
        "b": range(4),
    }
)
if index_kind == "range":
    keys = ["a"]
elif index_kind == "single":
    keys = ["a"]
    df = df.set_index(keys)
elif index_kind == "multi":
    keys = ["a", "a2"]
    df["a2"] = df["a"]
    df = df.set_index(keys)
args = get_groupby_method_args(reduction_func, df)
gb = df.groupby(keys, as_index=as_index, sort=sort, observed=observed)
op_result = getattr(gb, reduction_func)(*args)
if as_index:
    result = op_result.index.get_level_values("a").categories
else:
    result = op_result["a"].cat.categories
expected = Index([1, 4, 3, 2])
tm.assert_index_equal(result, expected)

if index_kind == "multi":
    result = op_result.index.get_level_values("a2").categories
    tm.assert_index_equal(result, expected)
