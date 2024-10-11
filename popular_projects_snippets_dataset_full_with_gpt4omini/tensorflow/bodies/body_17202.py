# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 6, 6, 1]
data = [
    128, 128, 64, 64, 128, 128, 64, 64, 64, 64, 128, 128, 64, 64, 128, 128,
    50, 50, 100, 100, 50, 50, 100, 100, 50, 50, 100, 100, 50, 50, 100, 100,
    50, 50, 100, 100
]
img_np = np.array(data, dtype=np.uint8).reshape(img_shape)

target_height = 8
target_width = 8
expected_data = [
    128, 135, 96, 55, 64, 114, 134, 128, 78, 81, 68, 52, 57, 118, 144, 136,
    55, 49, 79, 109, 103, 89, 83, 84, 74, 70, 95, 122, 115, 69, 49, 55, 100,
    105, 75, 43, 50, 89, 105, 100, 57, 54, 74, 96, 91, 65, 55, 58, 70, 69,
    75, 81, 80, 72, 69, 70, 105, 112, 75, 36, 45, 92, 111, 105
]

with self.cached_session():
    image = constant_op.constant(img_np, shape=img_shape)
    y = image_ops.resize_images(image, [target_height, target_width],
                                image_ops.ResizeMethodV1.BICUBIC)
    resized = self.evaluate(y)
    expected = np.array(expected_data).reshape(
        [1, target_height, target_width, 1])
    self.assertAllClose(resized, expected, atol=1)
