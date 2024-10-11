# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH8093 & GH26411
override_dtype = None

if (
    isinstance(values, Categorical)
    and not isinstance(columns, list)
    and op in ["sum", "prod", "skew"]
):
    # handled below GH#41291
    pass
elif (
    isinstance(values, Categorical)
    and len(keys) == 1
    and op in ["idxmax", "idxmin"]
):
    mark = pytest.mark.xfail(
        raises=ValueError, match="attempt to get arg(min|max) of an empty sequence"
    )
    request.node.add_marker(mark)
elif (
    isinstance(values, Categorical)
    and len(keys) == 1
    and not isinstance(columns, list)
):
    mark = pytest.mark.xfail(
        raises=TypeError, match="'Categorical' does not implement"
    )
    request.node.add_marker(mark)
elif isinstance(values, Categorical) and len(keys) == 1 and op in ["sum", "prod"]:
    mark = pytest.mark.xfail(
        raises=AssertionError, match="(DataFrame|Series) are different"
    )
    request.node.add_marker(mark)
elif (
    isinstance(values, Categorical)
    and len(keys) == 2
    and op in ["min", "max", "sum"]
):
    mark = pytest.mark.xfail(
        raises=AssertionError, match="(DataFrame|Series) are different"
    )
    request.node.add_marker(mark)

elif isinstance(values, BooleanArray) and op in ["sum", "prod"]:
    # We expect to get Int64 back for these
    override_dtype = "Int64"

if isinstance(values[0], bool) and op in ("prod", "sum"):
    # sum/product of bools is an integer
    override_dtype = "int64"

df = DataFrame({"A": values, "B": values, "C": values}, columns=list("ABC"))

if hasattr(values, "dtype"):
    # check that we did the construction right
    assert (df.dtypes == values.dtype).all()

df = df.iloc[:0]

gb = df.groupby(keys, group_keys=False, dropna=dropna)[columns]

def get_result(**kwargs):
    if method == "attr":
        exit(getattr(gb, op)(**kwargs))
    else:
        exit(getattr(gb, method)(op, **kwargs))

if columns == "C":
    # i.e. SeriesGroupBy
    if op in ["prod", "sum", "skew"]:
        # ops that require more than just ordered-ness
        if df.dtypes[0].kind == "M":
            # GH#41291
            # datetime64 -> prod and sum are invalid
            if op == "skew":
                msg = "does not support reduction 'skew'"
            else:
                msg = "datetime64 type does not support"
            with pytest.raises(TypeError, match=msg):
                get_result()

            exit()
    if op in ["prod", "sum", "skew"]:
        if isinstance(values, Categorical):
            # GH#41291
            if op == "skew":
                msg = f"does not support reduction '{op}'"
            else:
                msg = "category type does not support"
            with pytest.raises(TypeError, match=msg):
                get_result()

            exit()
else:
    # ie. DataFrameGroupBy
    if op in ["prod", "sum"]:
        # ops that require more than just ordered-ness
        if df.dtypes[0].kind == "M":
            # GH#41291
            # datetime64 -> prod and sum are invalid
            with pytest.raises(TypeError, match="datetime64 type does not support"):
                get_result()
            result = get_result(numeric_only=True)

            # with numeric_only=True, these are dropped, and we get
            # an empty DataFrame back
            expected = df.set_index(keys)[[]]
            tm.assert_equal(result, expected)
            exit()

        elif isinstance(values, Categorical):
            # GH#41291
            # Categorical doesn't implement sum or prod
            with pytest.raises(TypeError, match="category type does not support"):
                get_result()
            result = get_result(numeric_only=True)

            # with numeric_only=True, these are dropped, and we get
            # an empty DataFrame back
            expected = df.set_index(keys)[[]]
            if len(keys) != 1 and op == "prod":
                # TODO: why just prod and not sum?
                # Categorical is special without 'observed=True'
                lev = Categorical([0], dtype=values.dtype)
                mi = MultiIndex.from_product([lev, lev], names=["A", "B"])
                expected = DataFrame([], columns=[], index=mi)

            tm.assert_equal(result, expected)
            exit()

        elif df.dtypes[0] == object:
            result = get_result()
            expected = df.set_index(keys)[["C"]]
            tm.assert_equal(result, expected)
            exit()

    if (op in ["min", "max", "skew"] and isinstance(values, Categorical)) or (
        op == "skew" and df.dtypes[0].kind == "M"
    ):
        if op == "skew" or len(keys) == 1:
            msg = "|".join(
                [
                    "Categorical is not ordered",
                    "does not support reduction",
                ]
            )
            with pytest.raises(TypeError, match=msg):
                get_result()
            exit()
        # Categorical doesn't implement, so with numeric_only=True
        #  these are dropped and we get an empty DataFrame back
        result = get_result()

        # with numeric_only=True, these are dropped, and we get
        # an empty DataFrame back
        if len(keys) != 1:
            # Categorical is special without 'observed=True'
            lev = Categorical([0], dtype=values.dtype)
            mi = MultiIndex.from_product([lev, lev], names=keys)
            expected = DataFrame([], columns=[], index=mi)
        else:
            # all columns are dropped, but we end up with one row
            # Categorical is special without 'observed=True'
            lev = Categorical([0], dtype=values.dtype)
            ci = Index(lev, name=keys[0])
            expected = DataFrame([], columns=[], index=ci)

        tm.assert_equal(result, expected)
        exit()

result = get_result()
expected = df.set_index(keys)[columns]
if override_dtype is not None:
    expected = expected.astype(override_dtype)
if len(keys) == 1:
    expected.index.name = keys[0]
tm.assert_equal(result, expected)
