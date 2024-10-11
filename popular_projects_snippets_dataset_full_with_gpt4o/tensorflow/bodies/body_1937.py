# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
max_y = max(src_y - 1, 1) * (dst_y - 1) + 1
max_x = max(src_x - 1, 1) * (dst_x - 1) + 1

input_data = [
    range(y * max_x, (y + 1) * max_x, max(dst_x - 1, 1))
    for y in range(0, max_y, max(dst_y - 1, 1))
]

result = [
    range(y * max_x, (y + 1) * max_x, max(src_x - 1, 1))
    for y in range(0, max_y, max(src_y - 1, 1))
]

self._assertForwardOpMatchesExpected(
    np.array(input_data, dtype=dtype), [dst_y, dst_x],
    expected=np.array(result, dtype=np.float32),
    large_tolerance=True)
