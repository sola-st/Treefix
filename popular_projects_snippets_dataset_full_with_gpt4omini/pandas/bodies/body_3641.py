# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#30484
df = DataFrame({"x": range(5)})
expected = df.copy()
df["y"] = range(5)
y = df["y"]

with tm.assert_produces_warning(None):
    if inplace:
        df.drop("y", axis=1, inplace=inplace)
    else:
        df = df.drop("y", axis=1, inplace=inplace)

    # Perform operation and check result
    getattr(y, operation)(1)
    tm.assert_frame_equal(df, expected)
