# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame(
    np.zeros((200, 4)),
    columns=[str(i) for i in range(4)],
    index=[str(i) for i in range(200)],
    dtype=dtype,
)

data = df.to_json(orient=orient)
result = read_json(data, orient=orient, convert_axes=convert_axes, dtype=dtype)

expected = df.copy()
if not dtype:
    expected = expected.astype(np.int64)

# index columns, and records orients cannot fully preserve the string
# dtype for axes as the index and column labels are used as keys in
# JSON objects. JSON keys are by definition strings, so there's no way
# to disambiguate whether those keys actually were strings or numeric
# beforehand and numeric wins out.
if convert_axes and (orient in ("index", "columns")):
    expected.columns = expected.columns.astype(np.int64)
    expected.index = expected.index.astype(np.int64)
elif orient == "records" and convert_axes:
    expected.columns = expected.columns.astype(np.int64)
elif convert_axes and orient == "split":
    expected.columns = expected.columns.astype(np.int64)

assert_json_roundtrip_equal(result, expected, orient)
