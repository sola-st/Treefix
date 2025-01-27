# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
x_shapes = [
    [1, 2, 2, 3],
    [2, 1, 2, 3],
    [1, 2, 2, 3],
    [2, 5, 5, 3],
    [2, 1, 1, 3],
]
for x_shape in x_shapes:
    x_np = np.random.rand(*x_shape) * 255.
    contrast_factor = np.random.rand() * 2.0 + 0.1
    y_np = self._adjustContrastNp(x_np, contrast_factor)
    y_tf = self._adjustContrastTf(x_np, contrast_factor)
    self.assertAllClose(y_tf, y_np, rtol=1e-5, atol=1e-5)
