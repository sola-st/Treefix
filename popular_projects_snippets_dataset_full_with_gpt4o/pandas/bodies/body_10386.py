# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 36308

if transformation_func == "ngroup":
    msg = "ngroup fails with axis=1: #45986"
    request.node.add_marker(pytest.mark.xfail(reason=msg))

df = DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, index=["x", "y"])
args = get_groupby_method_args(transformation_func, df)
result = df.groupby([0, 0, 1], axis=1).transform(transformation_func, *args)
expected = df.T.groupby([0, 0, 1]).transform(transformation_func, *args).T

if transformation_func in ["diff", "shift"]:
    # Result contains nans, so transpose coerces to float
    expected["b"] = expected["b"].astype("int64")

# cumcount returns Series; the rest are DataFrame
tm.assert_equal(result, expected)
