# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py

index = pd.Index(["a", "b", "c", "d", "e"])
values = {
    "A": [0.0, 1.0, 2.0, 3.0, 4.0],
    "B": [0.0, 1.0, 0.0, 1.0, 0.0],
    "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
    "D": [True, False, True, False, True],
}

df = DataFrame(data=values, index=index)

data = df.to_json(orient=orient)
result = read_json(data, orient=orient, convert_axes=convert_axes)

expected = df.copy()
expected = expected.assign(**expected.select_dtypes("number").astype(np.int64))

assert_json_roundtrip_equal(result, expected, orient)
