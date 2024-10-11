# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
result = flatten_buffer(data)
expected = memoryview(data).tobytes("A")
assert result == expected
if isinstance(data, (bytes, bytearray)):
    assert result is data
elif isinstance(result, memoryview):
    assert result.ndim == 1
    assert result.format == "B"
    assert result.contiguous
    assert result.shape == (result.nbytes,)
