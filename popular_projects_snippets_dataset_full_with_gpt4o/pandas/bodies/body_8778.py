# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
import pyarrow as pa

array = pa if array == "pyarrow" else np

arr = array.array([1, 2, 3])
if chunked:
    if array is np:
        pytest.skip("chunked not applicable to numpy array")
    arr = pa.chunked_array(arr)
if array is np:
    msg = "Unsupported type '<class 'numpy.ndarray'>' for ArrowExtensionArray"
else:
    msg = re.escape(
        "ArrowStringArray requires a PyArrow (chunked) array of string type"
    )
with pytest.raises(ValueError, match=msg):
    ArrowStringArray(arr)
