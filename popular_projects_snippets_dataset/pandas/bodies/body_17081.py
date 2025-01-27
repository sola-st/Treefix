# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# GH 13660
typ1, vals1 = item
typ2, vals2 = item2

vals3 = vals2

# basically infer
exp_index_dtype = None
exp_series_dtype = None

if typ1 == typ2:
    # same dtype is tested in test_concatlike_same_dtypes
    exit()
elif typ1 == "category" or typ2 == "category":
    # The `vals1 + vals2` below fails bc one of these is a Categorical
    #  instead of a list; we have separate dedicated tests for categorical
    exit()

# specify expected dtype
if typ1 == "bool" and typ2 in ("int64", "float64"):
    # series coerces to numeric based on numpy rule
    # index doesn't because bool is object dtype
    exp_series_dtype = typ2
    mark = pytest.mark.xfail(reason="GH#39187 casting to object")
    request.node.add_marker(mark)
elif typ2 == "bool" and typ1 in ("int64", "float64"):
    exp_series_dtype = typ1
    mark = pytest.mark.xfail(reason="GH#39187 casting to object")
    request.node.add_marker(mark)
elif (
    typ1 == "datetime64[ns, US/Eastern]"
    or typ2 == "datetime64[ns, US/Eastern]"
    or typ1 == "timedelta64[ns]"
    or typ2 == "timedelta64[ns]"
):
    exp_index_dtype = object
    exp_series_dtype = object

exp_data = vals1 + vals2
exp_data3 = vals1 + vals2 + vals3

# ----- Index ----- #

# index.append
# GH#39817
res = Index(vals1).append(Index(vals2))
exp = Index(exp_data, dtype=exp_index_dtype)
tm.assert_index_equal(res, exp)

# 3 elements
res = Index(vals1).append([Index(vals2), Index(vals3)])
exp = Index(exp_data3, dtype=exp_index_dtype)
tm.assert_index_equal(res, exp)

# ----- Series ----- #

# series._append
# GH#39817
res = Series(vals1)._append(Series(vals2), ignore_index=True)
exp = Series(exp_data, dtype=exp_series_dtype)
tm.assert_series_equal(res, exp, check_index_type=True)

# concat
# GH#39817
res = pd.concat([Series(vals1), Series(vals2)], ignore_index=True)
tm.assert_series_equal(res, exp, check_index_type=True)

# 3 elements
# GH#39817
res = Series(vals1)._append([Series(vals2), Series(vals3)], ignore_index=True)
exp = Series(exp_data3, dtype=exp_series_dtype)
tm.assert_series_equal(res, exp)

# GH#39817
res = pd.concat(
    [Series(vals1), Series(vals2), Series(vals3)],
    ignore_index=True,
)
tm.assert_series_equal(res, exp)
