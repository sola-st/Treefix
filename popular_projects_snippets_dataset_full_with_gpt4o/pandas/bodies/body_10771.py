# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_subclass.py
# GH28330 -- preserve subclass through groupby operations

if isinstance(obj, Series) and groupby_func in {"corrwith"}:
    pytest.skip(f"Not applicable for Series and {groupby_func}")

grouped = obj.groupby(np.arange(0, 10))

# Groups should preserve subclass type
assert isinstance(grouped.get_group(0), type(obj))

args = get_groupby_method_args(groupby_func, obj)

result1 = getattr(grouped, groupby_func)(*args)
result2 = grouped.agg(groupby_func, *args)

# Reduction or transformation kernels should preserve type
slices = {"ngroup", "cumcount", "size"}
if isinstance(obj, DataFrame) and groupby_func in slices:
    assert isinstance(result1, tm.SubclassedSeries)
else:
    assert isinstance(result1, type(obj))

# Confirm .agg() groupby operations return same results
if isinstance(result1, DataFrame):
    tm.assert_frame_equal(result1, result2)
else:
    tm.assert_series_equal(result1, result2)
