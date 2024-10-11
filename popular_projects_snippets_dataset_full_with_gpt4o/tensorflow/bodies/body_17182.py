# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [10, 100, 80, 10]
x = np.random.uniform(size=x_shape)
for preserve_aspect_ratio in [True, False]:
    with self.subTest(preserve_aspect_ratio=preserve_aspect_ratio):
        expect_shape = [10, 250, 200, 10] if preserve_aspect_ratio \
            else [10, 250, 250, 10]
        self._assertResizeCheckShape(
            x,
            x_shape, [250, 250],
            expect_shape,
            preserve_aspect_ratio=preserve_aspect_ratio)
