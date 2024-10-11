# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
func = reduction_func

g = obj.groupby(np.repeat([0, 1], 3))

if func == "corrwith" and isinstance(obj, Series):  # GH#32293
    request.node.add_marker(
        pytest.mark.xfail(reason="TODO: implement SeriesGroupBy.corrwith")
    )

args = get_groupby_method_args(reduction_func, obj)
result = g.transform(func, *args)

# this is the *definition* of a transformation
tm.assert_index_equal(result.index, obj.index)

if func not in ("ngroup", "size") and obj.ndim == 2:
    # size/ngroup return a Series, unlike other transforms
    tm.assert_index_equal(result.columns, obj.columns)

# verify that values were broadcasted across each group
assert len(set(DataFrame(result).iloc[-3:, -1])) == 1
