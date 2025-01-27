# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 3, 2, 1]
data = [64, 32, 32, 64, 50, 100]
target_height = 6
target_width = 4
expected_data = {}
expected_data[image_ops.ResizeMethodV1.BILINEAR] = [
    64.0, 48.0, 32.0, 32.0, 48.0, 48.0, 48.0, 48.0, 32.0, 48.0, 64.0, 64.0,
    41.0, 61.5, 82.0, 82.0, 50.0, 75.0, 100.0, 100.0, 50.0, 75.0, 100.0,
    100.0
]
expected_data[image_ops.ResizeMethodV1.NEAREST_NEIGHBOR] = [
    64.0, 64.0, 32.0, 32.0, 64.0, 64.0, 32.0, 32.0, 32.0, 32.0, 64.0, 64.0,
    32.0, 32.0, 64.0, 64.0, 50.0, 50.0, 100.0, 100.0, 50.0, 50.0, 100.0,
    100.0
]
expected_data[image_ops.ResizeMethodV1.AREA] = [
    64.0, 64.0, 32.0, 32.0, 64.0, 64.0, 32.0, 32.0, 32.0, 32.0, 64.0, 64.0,
    32.0, 32.0, 64.0, 64.0, 50.0, 50.0, 100.0, 100.0, 50.0, 50.0, 100.0,
    100.0
]

for nptype in self.TYPES:
    for method in [
        image_ops.ResizeMethodV1.BILINEAR,
        image_ops.ResizeMethodV1.NEAREST_NEIGHBOR,
        image_ops.ResizeMethodV1.AREA
    ]:
        with self.cached_session():
            img_np = np.array(data, dtype=nptype).reshape(img_shape)
            image = constant_op.constant(img_np, shape=img_shape)
            y = image_ops.resize_images(
                image, [target_height, target_width], method, align_corners=False)
            resized = self.evaluate(y)
            expected = np.array(expected_data[method]).reshape(
                [1, target_height, target_width, 1])
            self.assertAllClose(resized, expected, atol=1e-05)
