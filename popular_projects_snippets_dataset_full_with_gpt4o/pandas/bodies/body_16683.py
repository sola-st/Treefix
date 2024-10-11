# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 10824
left = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])
right = DataFrame(columns=["x", "y", "z"])

exp_out = DataFrame(
    {
        "a": [1, 4, 7],
        "b": [2, 5, 8],
        "c": [3, 6, 9],
        "x": np.array([np.nan] * 3, dtype=object),
        "y": np.array([np.nan] * 3, dtype=object),
        "z": np.array([np.nan] * 3, dtype=object),
    },
    columns=["a", "b", "c", "x", "y", "z"],
)
exp_in = exp_out[0:0]  # make empty DataFrame keeping dtype
# result will have object dtype
exp_in.index = exp_in.index.astype(object)

def check1(exp, kwarg):
    result = merge(left, right, how="inner", **kwarg)
    tm.assert_frame_equal(result, exp)
    result = merge(left, right, how="right", **kwarg)
    tm.assert_frame_equal(result, exp)

def check2(exp, kwarg):
    result = merge(left, right, how="left", **kwarg)
    tm.assert_frame_equal(result, exp)
    result = merge(left, right, how="outer", **kwarg)
    tm.assert_frame_equal(result, exp)

    # TODO: should the next loop be un-indented? doing so breaks this test
    for kwarg in [
        {"left_index": True, "right_index": True},
        {"left_index": True, "right_on": "x"},
        {"left_on": "a", "right_index": True},
        {"left_on": "a", "right_on": "x"},
    ]:
        check1(exp_in, kwarg)
        check2(exp_out, kwarg)
