# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 3, 2, 1]
data = [64, 32, 32, 64, 50, 100]
target_height = 6
target_width = 4
expected_data = {}
expected_data[image_ops.ResizeMethod.BILINEAR] = [
    64.0, 56.0, 40.0, 32.0, 56.0, 52.0, 44.0, 40.0, 40.0, 44.0, 52.0, 56.0,
    36.5, 45.625, 63.875, 73.0, 45.5, 56.875, 79.625, 91.0, 50.0, 62.5,
    87.5, 100.0
]
expected_data[image_ops.ResizeMethod.NEAREST_NEIGHBOR] = [
    64.0, 64.0, 32.0, 32.0, 64.0, 64.0, 32.0, 32.0, 32.0, 32.0, 64.0, 64.0,
    32.0, 32.0, 64.0, 64.0, 50.0, 50.0, 100.0, 100.0, 50.0, 50.0, 100.0,
    100.0
]
expected_data[image_ops.ResizeMethod.AREA] = [
    64.0, 64.0, 32.0, 32.0, 64.0, 64.0, 32.0, 32.0, 32.0, 32.0, 64.0, 64.0,
    32.0, 32.0, 64.0, 64.0, 50.0, 50.0, 100.0, 100.0, 50.0, 50.0, 100.0,
    100.0
]
expected_data[image_ops.ResizeMethod.LANCZOS3] = [
    75.8294, 59.6281, 38.4313, 22.23, 60.6851, 52.0037, 40.6454, 31.964,
    35.8344, 41.0779, 47.9383, 53.1818, 24.6968, 43.0769, 67.1244, 85.5045,
    35.7939, 56.4713, 83.5243, 104.2017, 44.8138, 65.1949, 91.8603, 112.2413
]
expected_data[image_ops.ResizeMethod.LANCZOS5] = [
    77.5699, 60.0223, 40.6694, 23.1219, 61.8253, 51.2369, 39.5593, 28.9709,
    35.7438, 40.8875, 46.5604, 51.7041, 21.5942, 43.5299, 67.7223, 89.658,
    32.1213, 56.784, 83.984, 108.6467, 44.5802, 66.183, 90.0082, 111.6109
]
expected_data[image_ops.ResizeMethod.GAUSSIAN] = [
    61.1087, 54.6926, 41.3074, 34.8913, 54.6926, 51.4168, 44.5832, 41.3074,
    41.696, 45.2456, 52.6508, 56.2004, 39.4273, 47.0526, 62.9602, 70.5855,
    47.3008, 57.3042, 78.173, 88.1764, 51.4771, 62.3638, 85.0752, 95.9619
]
expected_data[image_ops.ResizeMethod.BICUBIC] = [
    70.1453, 59.0252, 36.9748, 25.8547, 59.3195, 53.3386, 41.4789, 35.4981,
    36.383, 41.285, 51.0051, 55.9071, 30.2232, 42.151, 65.8032, 77.731,
    41.6492, 55.823, 83.9288, 98.1026, 47.0363, 62.2744, 92.4903, 107.7284
]
expected_data[image_ops.ResizeMethod.MITCHELLCUBIC] = [
    66.0382, 56.6079, 39.3921, 29.9618, 56.7255, 51.9603, 43.2611, 38.4959,
    39.1828, 43.4664, 51.2864, 55.57, 34.6287, 45.1812, 64.4458, 74.9983,
    43.8523, 56.8078, 80.4594, 93.4149, 48.9943, 63.026, 88.6422, 102.6739
]
for nptype in self.TYPES:
    for method in expected_data:
        with self.cached_session():
            img_np = np.array(data, dtype=nptype).reshape(img_shape)
            image = constant_op.constant(img_np, shape=img_shape)
            y = image_ops.resize_images_v2(image, [target_height, target_width],
                                           method)
            resized = self.evaluate(y)
            expected = np.array(expected_data[method]).reshape(
                [1, target_height, target_width, 1])
            self.assertAllClose(resized, expected, atol=1e-04)
