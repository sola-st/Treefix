# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 10824
left = DataFrame(columns=["a", "b", "c"])
right = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["x", "y", "z"])

exp_out = DataFrame(
    {
        "a": np.array([np.nan] * 3, dtype=object),
        "b": np.array([np.nan] * 3, dtype=object),
        "c": np.array([np.nan] * 3, dtype=object),
        "x": [1, 4, 7],
        "y": [2, 5, 8],
        "z": [3, 6, 9],
    },
    columns=["a", "b", "c", "x", "y", "z"],
)
exp_in = exp_out[0:0]  # make empty DataFrame keeping dtype

def check1(exp, kwarg):
    result = merge(left, right, how="inner", **kwarg)
    tm.assert_frame_equal(result, exp)
    result = merge(left, right, how="left", **kwarg)
    tm.assert_frame_equal(result, exp)

def check2(exp, kwarg):
    result = merge(left, right, how="right", **kwarg)
    tm.assert_frame_equal(result, exp)
    result = merge(left, right, how="outer", **kwarg)
    tm.assert_frame_equal(result, exp)

for kwarg in [
    {"left_index": True, "right_index": True},
    {"left_index": True, "right_on": "x"},
]:
    check1(exp_in, kwarg)
    check2(exp_out, kwarg)

kwarg = {"left_on": "a", "right_index": True}
check1(exp_in, kwarg)
exp_out["a"] = [0, 1, 2]
check2(exp_out, kwarg)

kwarg = {"left_on": "a", "right_on": "x"}
check1(exp_in, kwarg)
exp_out["a"] = np.array([np.nan] * 3, dtype=object)
check2(exp_out, kwarg)
