# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
import pyarrow as pa

result = pa.array(list("abcde"))
expected = pa.array(expected)

if multiple_chunks:
    result = pa.chunked_array([result[:3], result[3:]])
    expected = pa.chunked_array([expected[:3], expected[3:]])

result = ArrowStringArray(result)
expected = ArrowStringArray(expected)

result[key] = value
tm.assert_equal(result, expected)
