# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 3, 2, 1]
data = [6, 3, 3, 6, 6, 9]
target_height = 5
target_width = 4
expected_data = {}
expected_data[image_ops.ResizeMethodV1.BILINEAR] = [
    6.0, 5.0, 4.0, 3.0, 4.5, 4.5, 4.5, 4.5, 3.0, 4.0, 5.0, 6.0, 4.5, 5.5,
    6.5, 7.5, 6.0, 7.0, 8.0, 9.0
]
expected_data[image_ops.ResizeMethodV1.NEAREST_NEIGHBOR] = [
    6.0, 6.0, 3.0, 3.0, 3.0, 3.0, 6.0, 6.0, 3.0, 3.0, 6.0, 6.0, 6.0, 6.0,
    9.0, 9.0, 6.0, 6.0, 9.0, 9.0
]
# TODO(b/37749740): Improve alignment of ResizeMethodV1.AREA when
# align_corners=True.
expected_data[image_ops.ResizeMethodV1.AREA] = [
    6.0, 6.0, 6.0, 3.0, 6.0, 6.0, 6.0, 3.0, 3.0, 3.0, 3.0, 6.0, 3.0, 3.0,
    3.0, 6.0, 6.0, 6.0, 6.0, 9.0
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
                image, [target_height, target_width], method, align_corners=True)
            resized = self.evaluate(y)
            expected = np.array(expected_data[method]).reshape(
                [1, target_height, target_width, 1])
            self.assertAllClose(resized, expected, atol=1e-05)
