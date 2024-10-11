# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame(
    [["a", "b"], ["c", "d"]],
    index=['index " 1', "index / 2"],
    columns=["a \\ b", "y / z"],
)

result = read_json(df.to_json(orient=orient), orient=orient)
expected = df.copy()

assert_json_roundtrip_equal(result, expected, orient)
