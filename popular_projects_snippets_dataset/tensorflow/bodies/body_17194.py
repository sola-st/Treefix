# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img_shape = [1, 6, 4, 1]
single_shape = [6, 4, 1]
# This test is also conducted with int8, so 127 is the maximum
# value that can be used.
data = [
    127, 127, 64, 64, 127, 127, 64, 64, 64, 64, 127, 127, 64, 64, 127, 127,
    50, 50, 100, 100, 50, 50, 100, 100
]

def resize_func(t, new_size, method):
    exit(image_ops.resize_images(t, new_size, method))

img_np = np.array(data, dtype=np.uint8).reshape(img_shape)

for method in self.METHODS:
    with self.cached_session():
        image = constant_op.constant(img_np, shape=img_shape)
        y = resize_func(image, [6, 4], method)
        yshape = array_ops.shape(y)
        resized, newshape = self.evaluate([y, yshape])
        self.assertAllEqual(img_shape, newshape)
        self.assertAllClose(resized, img_np, atol=1e-5)

    # Resizing with a single image must leave the shape unchanged also.
with self.cached_session():
    img_single = img_np.reshape(single_shape)
    image = constant_op.constant(img_single, shape=single_shape)
    y = resize_func(image, [6, 4], self.METHODS[0])
    yshape = array_ops.shape(y)
    resized, newshape = self.evaluate([y, yshape])
    self.assertAllEqual(single_shape, newshape)
    self.assertAllClose(resized, img_single, atol=1e-5)

# Incorrect shape.
with self.assertRaises(ValueError):
    new_size = constant_op.constant(4)
    _ = resize_func(image, new_size, image_ops.ResizeMethodV1.BILINEAR)
with self.assertRaises(ValueError):
    new_size = constant_op.constant([4])
    _ = resize_func(image, new_size, image_ops.ResizeMethodV1.BILINEAR)
with self.assertRaises(ValueError):
    new_size = constant_op.constant([1, 2, 3])
    _ = resize_func(image, new_size, image_ops.ResizeMethodV1.BILINEAR)

# Incorrect dtypes.
with self.assertRaises(ValueError):
    new_size = constant_op.constant([6.0, 4])
    _ = resize_func(image, new_size, image_ops.ResizeMethodV1.BILINEAR)
with self.assertRaises(ValueError):
    _ = resize_func(image, [6, 4.0], image_ops.ResizeMethodV1.BILINEAR)
with self.assertRaises(ValueError):
    _ = resize_func(image, [None, 4], image_ops.ResizeMethodV1.BILINEAR)
with self.assertRaises(ValueError):
    _ = resize_func(image, [6, None], image_ops.ResizeMethodV1.BILINEAR)
