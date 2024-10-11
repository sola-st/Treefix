# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
"""
        This test will fail for:
            period:
                since period isn't yet implemented in ``select_dtypes``
                and because it will need a custom value converter +
                tick formatter (as was done for x-axis plots)

            categorical:
                 because it will need a custom value converter +
                 tick formatter (also doesn't work for x-axis, as of now)

            datetime_mixed_tz:
                because of the way how pandas handles ``Series`` of
                ``datetime`` objects with different timezone,
                generally converting ``datetime`` objects in a tz-aware
                form could help with this problem
        """
data = {
    "numeric": np.array([1, 2, 5]),
    "period": [
        pd.Period("2017-08-01 00:00:00", freq="H"),
        pd.Period("2017-08-01 02:00", freq="H"),
        pd.Period("2017-08-02 00:00:00", freq="H"),
    ],
    "categorical": pd.Categorical(
        ["c", "b", "a"], categories=["a", "b", "c"], ordered=False
    ),
    "datetime_mixed_tz": [
        pd.to_datetime("2017-08-01 00:00:00", utc=True),
        pd.to_datetime("2017-08-01 02:00:00"),
        pd.to_datetime("2017-08-02 00:00:00"),
    ],
}
testdata = DataFrame(data)
ax_period = testdata.plot(x="numeric", y="period")
assert (
    ax_period.get_lines()[0].get_data()[1] == testdata["period"].values
).all()
ax_categorical = testdata.plot(x="numeric", y="categorical")
assert (
    ax_categorical.get_lines()[0].get_data()[1]
    == testdata["categorical"].values
).all()
ax_datetime_mixed_tz = testdata.plot(x="numeric", y="datetime_mixed_tz")
assert (
    ax_datetime_mixed_tz.get_lines()[0].get_data()[1]
    == testdata["datetime_mixed_tz"].values
).all()
