# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 38774, GH 38815
grouped = df.groupby("A")

no_drop_nuisance = ("var", "std", "sem", "mean", "prod", "median")
if agg_function in no_drop_nuisance and not numeric_only:
    # Added numeric_only as part of GH#46560; these do not drop nuisance
    # columns when numeric_only is False
    klass = ValueError if agg_function in ("std", "sem") else TypeError
    msg = "|".join(["[C|c]ould not convert", "can't multiply sequence"])
    with pytest.raises(klass, match=msg):
        getattr(grouped, agg_function)(numeric_only=numeric_only)
else:
    result = getattr(grouped, agg_function)(numeric_only=numeric_only)
    if not numeric_only and agg_function == "sum":
        # sum is successful on column B
        columns = ["A", "B", "C", "D"]
    else:
        columns = ["A", "C", "D"]
    expected = getattr(df.loc[:, columns].groupby("A"), agg_function)(
        numeric_only=numeric_only
    )
    tm.assert_frame_equal(result, expected)
