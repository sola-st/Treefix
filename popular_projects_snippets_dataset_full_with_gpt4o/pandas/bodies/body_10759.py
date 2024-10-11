# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 4792
prices = {
    Timestamp("2011-01-06 10:59:05", tz=None): 24990,
    Timestamp("2011-01-06 12:43:33", tz=None): 25499,
    Timestamp("2011-01-06 12:54:09", tz=None): 25499,
}
volumes = {
    Timestamp("2011-01-06 10:59:05", tz=None): 1500000000,
    Timestamp("2011-01-06 12:43:33", tz=None): 5000000000,
    Timestamp("2011-01-06 12:54:09", tz=None): 100000000,
}
df = DataFrame({"PRICE": prices, "VOLUME": volumes})
result = df.groupby("PRICE").VOLUME.describe()
data = [
    df[df.PRICE == 24990].VOLUME.describe().values.tolist(),
    df[df.PRICE == 25499].VOLUME.describe().values.tolist(),
]
expected = DataFrame(
    data,
    index=Index([24990, 25499], name="PRICE"),
    columns=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
)
tm.assert_frame_equal(result, expected)
