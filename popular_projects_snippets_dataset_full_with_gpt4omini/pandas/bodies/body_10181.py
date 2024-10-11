# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 39433
data = [
    ["A", "2018-01-01", 100.0],
    ["A", "2018-01-02", 200.0],
    ["B", "2018-01-01", 150.0],
    ["B", "2018-01-02", 250.0],
]
df = DataFrame(data, columns=["id", "date", "num"])
df["date"] = to_datetime(df["date"])
df = df.set_index(["date"])

gp_by = [getattr(df, attr) for attr in by]
result = (
    df.groupby(gp_by, as_index=False).rolling(window=2, min_periods=1).mean()
)

expected = {"id": ["A", "A", "B", "B"]}
expected.update(expected_data)
expected = DataFrame(
    expected,
    index=df.index,
)
tm.assert_frame_equal(result, expected)
