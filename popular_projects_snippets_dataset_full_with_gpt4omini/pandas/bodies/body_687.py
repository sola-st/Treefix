# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

result = lib.maybe_convert_objects(
    np.array(idx, dtype=object),
    convert_period=True,
    convert_interval=True,
)
tm.assert_extension_array_equal(result, idx._data)
