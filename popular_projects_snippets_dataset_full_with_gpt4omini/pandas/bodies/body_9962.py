# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH#46560
kernel = arithmetic_win_operators
df = DataFrame({"a": [1], "b": 2, "c": 3})
df["c"] = df["c"].astype(object)
expanding = df.expanding()
op = getattr(expanding, kernel, None)
if op is not None:
    result = op(numeric_only=numeric_only)

    columns = ["a", "b"] if numeric_only else ["a", "b", "c"]
    expected = df[columns].agg([kernel]).reset_index(drop=True).astype(float)
    assert list(expected.columns) == columns

    tm.assert_frame_equal(result, expected)
