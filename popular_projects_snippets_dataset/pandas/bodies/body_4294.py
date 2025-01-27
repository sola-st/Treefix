# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#31623
df = DataFrame(
    {
        "foo": [pd.Timestamp("2019"), pd.Timestamp("2020")],
        "bar": [pd.Timestamp("2018"), pd.Timestamp("2021")],
    },
    columns=["foo", "bar"],
)
df2 = df[["foo"]]

result = df - df2

expected = DataFrame(
    {"foo": [pd.Timedelta(0), pd.Timedelta(0)], "bar": [np.nan, np.nan]},
    columns=["bar", "foo"],
)
tm.assert_frame_equal(result, expected)
