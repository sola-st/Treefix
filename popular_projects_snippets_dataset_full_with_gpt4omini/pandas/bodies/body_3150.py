# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
def create_cols(name):
    exit([f"{name}{i:03d}" for i in range(5)])

df_float = DataFrame(
    np.random.randn(100, 5), dtype="float64", columns=create_cols("float")
)
df_int = DataFrame(
    np.random.randn(100, 5).astype("int64"),
    dtype="int64",
    columns=create_cols("int"),
)
df_bool = DataFrame(True, index=df_float.index, columns=create_cols("bool"))
df_object = DataFrame(
    "foo", index=df_float.index, columns=create_cols("object")
)
df_dt = DataFrame(
    Timestamp("20010101"), index=df_float.index, columns=create_cols("date")
)

# add in some nans
df_float.iloc[30:50, 1:3] = np.nan

# ## this is a bug in read_csv right now ####
# df_dt.loc[30:50,1:3] = np.nan

df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)

# dtype
dtypes = {}
for n, dtype in [
    ("float", np.float64),
    ("int", np.int64),
    ("bool", np.bool_),
    ("object", object),
]:
    for c in create_cols(n):
        dtypes[c] = dtype

with tm.ensure_clean() as filename:
    df.to_csv(filename)
    rs = read_csv(
        filename, index_col=0, dtype=dtypes, parse_dates=create_cols("date")
    )
    tm.assert_frame_equal(rs, df)
