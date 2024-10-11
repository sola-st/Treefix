# Extracted from ./data/repos/pandas/pandas/tests/base/test_transpose.py
# GH 42380
df = DataFrame(data, index=index, columns=columns, dtype=dtype)
result = df.T
expected = DataFrame(transposed_data, index=columns, columns=index, dtype=dtype)
tm.assert_frame_equal(result, expected)
