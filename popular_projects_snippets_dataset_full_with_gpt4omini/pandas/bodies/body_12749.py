# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py

dtype = np.int64

df = DataFrame(
    [[1, 2, 3], [4, 5, 6]],
    index=["a", "b"],
    columns=["x", "y", "z"],
    dtype=dtype,
)
encode_kwargs = {} if orient is None else {"orient": orient}
assert (df.dtypes == dtype).all()

output = ujson.decode(ujson.encode(df, **encode_kwargs))
assert (df.dtypes == dtype).all()

# Ensure proper DataFrame initialization.
if orient == "split":
    dec = _clean_dict(output)
    output = DataFrame(**dec)
else:
    output = DataFrame(output)

# Corrections to enable DataFrame comparison.
if orient == "values":
    df.columns = [0, 1, 2]
    df.index = [0, 1]
elif orient == "records":
    df.index = [0, 1]
elif orient == "index":
    df = df.transpose()

assert (df.dtypes == dtype).all()
tm.assert_frame_equal(output, df)
