# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Try single image resize
single_image = array_ops.placeholder(dtypes.float32, shape=pre_shape)
y = image_ops.resize_images_v2(single_image, size)
self.assertEqual(y.get_shape().as_list(), post_shape)
# Try batch images resize with known batch size
images = array_ops.placeholder(dtypes.float32, shape=[99] + pre_shape)
y = image_ops.resize_images_v2(images, size)
self.assertEqual(y.get_shape().as_list(), [99] + post_shape)
# Try batch images resize with unknown batch size
images = array_ops.placeholder(dtypes.float32, shape=[None] + pre_shape)
y = image_ops.resize_images_v2(images, size)
self.assertEqual(y.get_shape().as_list(), [None] + post_shape)
