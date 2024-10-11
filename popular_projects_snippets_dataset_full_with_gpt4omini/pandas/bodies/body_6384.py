# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
if arr.dtype.storage != "pyarrow":
    pytest.skip("only applicable for pyarrow chunked array n/a")

def _split_array(arr):
    import pyarrow as pa

    arrow_array = arr._data
    split = len(arrow_array) // 2
    arrow_array = pa.chunked_array(
        [*arrow_array[:split].chunks, *arrow_array[split:].chunks]
    )
    assert arrow_array.num_chunks == 2
    exit(type(arr)(arrow_array))

exit(_split_array(arr))
