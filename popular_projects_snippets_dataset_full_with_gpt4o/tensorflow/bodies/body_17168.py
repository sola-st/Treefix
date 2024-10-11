# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 6, 4, 1]
# This test is also conducted with int8, so 127 is the maximum
# value that can be used.
data = [
    127, 127, 64, 64, 127, 127, 64, 64, 64, 64, 127, 127, 64, 64, 127, 127,
    50, 50, 100, 100, 50, 50, 100, 100
]
# Test size where width is specified as a tensor which is a sum
# of two tensors.
width_1 = constant_op.constant(1)
width_2 = constant_op.constant(3)
width = math_ops.add(width_1, width_2)
height = constant_op.constant(6)

img_np = np.array(data, dtype=np.uint8).reshape(img_shape)

for method in self.METHODS:
    with self.cached_session():
        image = constant_op.constant(img_np, shape=img_shape)
        y = image_ops.resize_images_v2(image, [height, width], method)
        yshape = array_ops.shape(y)
        resized, newshape = self.evaluate([y, yshape])
        self.assertAllEqual(img_shape, newshape)
        if method in self.INTERPOLATING_METHODS:
            self.assertAllClose(resized, img_np, atol=1e-5)
