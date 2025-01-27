# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# 4-D input with batch dimension.
x_np = np.array(
    [[1, 2, 3], [4, 10, 1]], dtype=np.uint8).reshape([1, 1, 2, 3])
self._TestRGBToGrayscale(x_np)

# 3-D input with no batch dimension.
x_np = np.array([[1, 2, 3], [4, 10, 1]], dtype=np.uint8).reshape([1, 2, 3])
self._TestRGBToGrayscale(x_np)
