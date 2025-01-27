# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH#36327
if (
    reduction_func in ("idxmin", "idxmax")
    and not observed
    and index_kind != "multi"
):
    msg = "GH#10694 - idxmin/max broken for categorical with observed=False"
    request.node.add_marker(pytest.mark.xfail(reason=msg))

# Ensure there is at least one null value by appending to the end
values = np.append(np.random.choice([1, 2, None], size=19), None)
df = pd.DataFrame(
    {"x": pd.Categorical(values, categories=[1, 2, 3]), "y": range(20)}
)

# Strategy: Compare to dropna=True by filling null values with a new code
df_filled = df.copy()
df_filled["x"] = pd.Categorical(values, categories=[1, 2, 3, 4]).fillna(4)

if index_kind == "range":
    keys = ["x"]
elif index_kind == "single":
    keys = ["x"]
    df = df.set_index("x")
    df_filled = df_filled.set_index("x")
else:
    keys = ["x", "x2"]
    df["x2"] = df["x"]
    df = df.set_index(["x", "x2"])
    df_filled["x2"] = df_filled["x"]
    df_filled = df_filled.set_index(["x", "x2"])
args = get_groupby_method_args(reduction_func, df)
args_filled = get_groupby_method_args(reduction_func, df_filled)
if reduction_func == "corrwith" and index_kind == "range":
    # Don't include the grouping columns so we can call reset_index
    args = (args[0].drop(columns=keys),)
    args_filled = (args_filled[0].drop(columns=keys),)

gb_filled = df_filled.groupby(keys, observed=observed, sort=sort, as_index=True)
expected = getattr(gb_filled, reduction_func)(*args_filled).reset_index()
expected["x"] = expected["x"].replace(4, None)
if index_kind == "multi":
    expected["x2"] = expected["x2"].replace(4, None)
if as_index:
    if index_kind == "multi":
        expected = expected.set_index(["x", "x2"])
    else:
        expected = expected.set_index("x")
else:
    if index_kind != "range" and reduction_func != "size":
        # size, unlike other methods, has the desired behavior in GH#49519
        expected = expected.drop(columns="x")
        if index_kind == "multi":
            expected = expected.drop(columns="x2")
if reduction_func in ("idxmax", "idxmin") and index_kind != "range":
    # expected was computed with a RangeIndex; need to translate to index values
    values = expected["y"].values.tolist()
    if index_kind == "single":
        values = [np.nan if e == 4 else e for e in values]
    else:
        values = [(np.nan, np.nan) if e == (4, 4) else e for e in values]
    expected["y"] = values
if reduction_func == "size":
    # size, unlike other methods, has the desired behavior in GH#49519
    expected = expected.rename(columns={0: "size"})
    if as_index:
        expected = expected["size"].rename(None)

gb_keepna = df.groupby(
    keys, dropna=False, observed=observed, sort=sort, as_index=as_index
)
result = getattr(gb_keepna, reduction_func)(*args)

# size will return a Series, others are DataFrame
tm.assert_equal(result, expected)
