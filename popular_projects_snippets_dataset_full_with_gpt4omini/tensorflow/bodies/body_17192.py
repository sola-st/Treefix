# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 6, 4, 1]
single_shape = [6, 4, 1]
# This test is also conducted with int8, so 127 is the maximum
# value that can be used.
data = [
    127, 127, 64, 64, 127, 127, 64, 64, 64, 64, 127, 127, 64, 64, 127, 127,
    50, 50, 100, 100, 50, 50, 100, 100
]
target_height = 6
target_width = 4

for nptype in self.TYPES:
    img_np = np.array(data, dtype=nptype).reshape(img_shape)

    for method in self.METHODS:
        with self.cached_session():
            image = constant_op.constant(img_np, shape=img_shape)
            y = image_ops.resize_images(image, [target_height, target_width],
                                        method)
            yshape = array_ops.shape(y)
            resized, newshape = self.evaluate([y, yshape])
            self.assertAllEqual(img_shape, newshape)
            self.assertAllClose(resized, img_np, atol=1e-5)

      # Resizing with a single image must leave the shape unchanged also.
    with self.cached_session():
        img_single = img_np.reshape(single_shape)
        image = constant_op.constant(img_single, shape=single_shape)
        y = image_ops.resize_images(image, [target_height, target_width],
                                    self.METHODS[0])
        yshape = array_ops.shape(y)
        newshape = self.evaluate(yshape)
        self.assertAllEqual(single_shape, newshape)
