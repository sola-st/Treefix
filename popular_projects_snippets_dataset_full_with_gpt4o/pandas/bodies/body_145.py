# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
df = DataFrame(**{ax: ["a", "b", "c"]})

with np.errstate(all="ignore"):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("ignore", RuntimeWarning)
        test_res = func(np.array([], dtype="f8"))
    is_reduction = not isinstance(test_res, np.ndarray)

    result = df.apply(func, axis=axis, raw=raw)
    if is_reduction:
        agg_axis = df._get_agg_axis(axis)
        assert isinstance(result, Series)
        assert result.index is agg_axis
    else:
        assert isinstance(result, DataFrame)
