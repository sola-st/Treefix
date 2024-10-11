# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 36040
df = DataFrame({"group": ["A"] * 10 + ["B"] * 10, "data": range(20)})

window_size = 5
result = (
    df.groupby("group")
    .rolling(window_size, center=True, min_periods=min_periods)
    .mean()
)
result = result.reset_index()[["group", "data"]]

grp_A_mean = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.5, 8.0]
grp_B_mean = [x + 10.0 for x in grp_A_mean]

num_nans = max(0, min_periods - 3)  # For window_size of 5
nans = [np.nan] * num_nans
grp_A_expected = nans + grp_A_mean[num_nans : 10 - num_nans] + nans
grp_B_expected = nans + grp_B_mean[num_nans : 10 - num_nans] + nans

expected = DataFrame(
    {"group": ["A"] * 10 + ["B"] * 10, "data": grp_A_expected + grp_B_expected}
)

tm.assert_frame_equal(result, expected)
