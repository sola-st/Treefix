# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
# protocol added in 0.15.0
import pyarrow as pa

data = pd.array(["a", "b", "c"], dtype=dtype)
arr = pa.array(data)
expected = pa.array(list(data), type=pa.string(), from_pandas=True)
if dtype.storage == "pyarrow":
    expected = pa.chunked_array(expected)

assert arr.equals(expected)
