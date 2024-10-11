# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 6, 6, 1]
data = [
    128, 64, 32, 16, 8, 4, 4, 8, 16, 32, 64, 128, 128, 64, 32, 16, 8, 4, 5,
    10, 15, 20, 25, 30, 30, 25, 20, 15, 10, 5, 5, 10, 15, 20, 25, 30
]
img_np = np.array(data, dtype=np.uint8).reshape(img_shape)

target_height = 4
target_width = 4
expected_data = [
    73, 33, 23, 39, 73, 33, 23, 39, 14, 16, 19, 21, 14, 16, 19, 21
]

with self.cached_session():
    image = constant_op.constant(img_np, shape=img_shape)
    y = image_ops.resize_images_v2(image, [target_height, target_width],
                                   image_ops.ResizeMethod.AREA)
    expected = np.array(expected_data).reshape(
        [1, target_height, target_width, 1])
    resized = self.evaluate(y)
    self.assertAllClose(resized, expected, atol=1)
