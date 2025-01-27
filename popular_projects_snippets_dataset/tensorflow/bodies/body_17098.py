# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [2, 2, 3]
x_data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
x_np = np.array(x_data, dtype=np.uint8).reshape(x_shape)

y_data = [0, 0, 3, 44, 125, 216, 27, 0, 224, 80, 245, 0]
y_np = np.array(y_data, dtype=np.uint8).reshape(x_shape)

self._testBrightness(x_np, y_np, delta=-10. / 255.)
