# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH50248
orig = data.copy()

result = orig.copy()
result[:] = data[0]
expected = ArrowExtensionArray(
    pa.array([data[0]] * len(data), type=data._data.type)
)
tm.assert_extension_array_equal(result, expected)

result = orig.copy()
result[:] = data[::-1]
expected = data[::-1]
tm.assert_extension_array_equal(result, expected)

result = orig.copy()
result[:] = data.tolist()
expected = data
tm.assert_extension_array_equal(result, expected)
