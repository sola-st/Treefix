# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# TODO: create a better frame to test with and improve coverage
if orient in ("index", "columns"):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"Can't have duplicate index values for orient '{orient}')"
        )
    )

data = categorical_frame.to_json(orient=orient)

result = read_json(data, orient=orient, convert_axes=convert_axes)

expected = categorical_frame.copy()
expected.index = expected.index.astype(str)  # Categorical not preserved
expected.index.name = None  # index names aren't preserved in JSON
assert_json_roundtrip_equal(result, expected, orient)
