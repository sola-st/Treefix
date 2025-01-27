# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# dups across blocks
df_float = DataFrame(np.random.randn(10, 3), dtype="float64")
df_int = DataFrame(np.random.randn(10, 3).astype("int64"))
df_bool = DataFrame(True, index=df_float.index, columns=df_float.columns)
df_object = DataFrame("foo", index=df_float.index, columns=df_float.columns)
df_dt = DataFrame(
    pd.Timestamp("20010101"), index=df_float.index, columns=df_float.columns
)
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)

if not using_array_manager:
    assert len(df._mgr.blknos) == len(df.columns)
    assert len(df._mgr.blklocs) == len(df.columns)

# testing iloc
for i in range(len(df.columns)):
    df.iloc[:, i]
