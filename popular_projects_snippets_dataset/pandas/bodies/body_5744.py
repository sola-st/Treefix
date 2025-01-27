# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# https://github.com/pandas-dev/pandas/pull/47034#discussion_r955500784
# data._data = pa.ChunkedArray
result = type(data)._from_sequence(data._data)
tm.assert_extension_array_equal(result, data)
assert isinstance(result._data, pa.ChunkedArray)

result = type(data)._from_sequence(data._data.combine_chunks())
tm.assert_extension_array_equal(result, data)
assert isinstance(result._data, pa.ChunkedArray)
