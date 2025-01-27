# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
df = DataFrame(
    {
        "a": list("abc"),
        "b": list(range(1, 4)),
        "c": np.arange(3, 6).astype("u1"),
        "d": np.arange(4.0, 7.0, dtype="float64"),
        "e": [True, False, True],
        "f": pd.date_range("now", periods=3).values,
    }
)
df["g"] = df.f.diff()
assert not hasattr(np, "u8")
r = df.select_dtypes(include=["i8", "O"], exclude=["timedelta"])
e = df[["a", "b"]]
tm.assert_frame_equal(r, e)

r = df.select_dtypes(include=["i8", "O", "timedelta64[ns]"])
e = df[["a", "b", "g"]]
tm.assert_frame_equal(r, e)
