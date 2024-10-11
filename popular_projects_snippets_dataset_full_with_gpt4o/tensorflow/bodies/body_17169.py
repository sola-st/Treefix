# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# This test is also conducted with int8, so 127 is the maximum
# value that can be used.
data = [
    127, 127, 64, 64, 127, 127, 64, 64, 64, 64, 127, 127, 64, 64, 127, 127,
    50, 50, 100, 100, 50, 50, 100, 100
]
expected_data = [127, 64, 64, 127, 50, 100]
target_height = 3
target_width = 2

# Test out 3-D and 4-D image shapes.
img_shapes = [[1, 6, 4, 1], [6, 4, 1]]
target_shapes = [[1, target_height, target_width, 1],
                 [target_height, target_width, 1]]

for target_shape, img_shape in zip(target_shapes, img_shapes):

    for nptype in self.TYPES:
        img_np = np.array(data, dtype=nptype).reshape(img_shape)

        for method in self.METHODS:
            if test.is_gpu_available() and self.shouldRunOnGPU(method, nptype):
                with self.cached_session():
                    image = constant_op.constant(img_np, shape=img_shape)
                    y = image_ops.resize_images_v2(
                        image, [target_height, target_width], method)
                    expected = np.array(expected_data).reshape(target_shape)
                    resized = self.evaluate(y)
                    self.assertAllClose(resized, expected, atol=1e-5)
