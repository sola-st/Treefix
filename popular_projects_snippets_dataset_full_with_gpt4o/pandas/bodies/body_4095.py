# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH 40346
df = DataFrame(
    {
        "ID": [100, 100, 100, 200, 200, 200],
        "value": [0, 0, 0, 1, 2, 0],
    },
    dtype="Int64",
)
df = df.groupby("ID")

result = getattr(df, op)()
expected = DataFrame(
    {"value": expected_value},
    index=Index([100, 200], name="ID", dtype="Int64"),
)
tm.assert_frame_equal(result, expected)
