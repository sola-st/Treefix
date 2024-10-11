# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
if groupby_func in ("idxmax", "idxmin"):
    pytest.skip("idxmax and idx_min tested in test_idxmin_idxmax_axis1")
if groupby_func in ("corrwith", "skew"):
    msg = "GH#47723 groupby.corrwith and skew do not correctly implement axis=1"
    request.node.add_marker(pytest.mark.xfail(reason=msg))

df = DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df["E"] = "x"
groups = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
gb = df.groupby(groups)
method = getattr(gb, groupby_func)
args = get_groupby_method_args(groupby_func, df)
kwargs = {"axis": 1}
if numeric_only is not None:
    # when numeric_only is None we don't pass any argument
    kwargs["numeric_only"] = numeric_only

# Functions without numeric_only and axis args
no_args = ("cumprod", "cumsum", "diff", "fillna", "pct_change", "rank", "shift")
# Functions with axis args
has_axis = (
    "cumprod",
    "cumsum",
    "diff",
    "pct_change",
    "rank",
    "shift",
    "cummax",
    "cummin",
    "idxmin",
    "idxmax",
    "fillna",
)
if numeric_only is not None and groupby_func in no_args:
    msg = "got an unexpected keyword argument 'numeric_only'"
    with pytest.raises(TypeError, match=msg):
        method(*args, **kwargs)
elif groupby_func not in has_axis:
    msg = "got an unexpected keyword argument 'axis'"
    with pytest.raises(TypeError, match=msg):
        method(*args, **kwargs)
    # fillna and shift are successful even on object dtypes
elif (numeric_only is None or not numeric_only) and groupby_func not in (
    "fillna",
    "shift",
):
    msgs = (
        # cummax, cummin, rank
        "not supported between instances of",
        # cumprod
        "can't multiply sequence by non-int of type 'float'",
        # cumsum, diff, pct_change
        "unsupported operand type",
    )
    with pytest.raises(TypeError, match=f"({'|'.join(msgs)})"):
        method(*args, **kwargs)
else:
    result = method(*args, **kwargs)

    df_expected = df.drop(columns="E").T if numeric_only else df.T
    expected = getattr(df_expected, groupby_func)(*args).T
    if groupby_func == "shift" and not numeric_only:
        # shift with axis=1 leaves the leftmost column as numeric
        # but transposing for expected gives us object dtype
        expected = expected.astype(float)

    tm.assert_equal(result, expected)
