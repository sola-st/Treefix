# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

df = DataFrame(
    np.random.randn(1000, 30),
    columns=list(range(15)) + list(range(15)),
    dtype="float64",
)

with tm.ensure_clean() as filename:
    df.to_csv(filename)  # single dtype, fine
    result = read_csv(filename, index_col=0)
    result.columns = df.columns
    tm.assert_frame_equal(result, df)

df_float = DataFrame(np.random.randn(1000, 3), dtype="float64")
df_int = DataFrame(np.random.randn(1000, 3)).astype("int64")
df_bool = DataFrame(True, index=df_float.index, columns=range(3))
df_object = DataFrame("foo", index=df_float.index, columns=range(3))
df_dt = DataFrame(Timestamp("20010101"), index=df_float.index, columns=range(3))
df = pd.concat(
    [df_float, df_int, df_bool, df_object, df_dt], axis=1, ignore_index=True
)

df.columns = [0, 1, 2] * 5

with tm.ensure_clean() as filename:
    df.to_csv(filename)
    result = read_csv(filename, index_col=0)

    # date cols
    for i in ["0.4", "1.4", "2.4"]:
        result[i] = to_datetime(result[i])

    result.columns = df.columns
    tm.assert_frame_equal(result, df)

# GH3457

N = 10
df = tm.makeCustomDataframe(N, 3)
df.columns = ["a", "a", "b"]

with tm.ensure_clean() as filename:
    df.to_csv(filename)

    # read_csv will rename the dups columns
    result = read_csv(filename, index_col=0)
    result = result.rename(columns={"a.1": "a"})
    tm.assert_frame_equal(result, df)
