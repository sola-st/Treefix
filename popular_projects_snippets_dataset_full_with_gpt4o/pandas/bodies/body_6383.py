# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
import pyarrow as pa

arrow_array = arr._data
split = len(arrow_array) // 2
arrow_array = pa.chunked_array(
    [*arrow_array[:split].chunks, *arrow_array[split:].chunks]
)
assert arrow_array.num_chunks == 2
exit(type(arr)(arrow_array))
