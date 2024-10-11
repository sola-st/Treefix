# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 10295
# Verify that NaT is not in the result of max, min, first and last on
# Dataframe with datetime or timedelta values.
df_test = DataFrame(
    {
        "dt": [
            np.nan,
            "2015-07-24 10:10",
            "2015-07-25 11:11",
            "2015-07-23 12:12",
            np.nan,
        ],
        "td": [
            np.nan,
            timedelta(days=1),
            timedelta(days=2),
            timedelta(days=3),
            np.nan,
        ],
    }
)
df_test.dt = pd.to_datetime(df_test.dt)
df_test["group"] = "A"
df_ref = df_test[df_test.dt.notna()]

grouped_test = df_test.groupby("group")
grouped_ref = df_ref.groupby("group")

tm.assert_frame_equal(grouped_ref.max(), grouped_test.max())
tm.assert_frame_equal(grouped_ref.min(), grouped_test.min())
tm.assert_frame_equal(grouped_ref.first(), grouped_test.first())
tm.assert_frame_equal(grouped_ref.last(), grouped_test.last())
