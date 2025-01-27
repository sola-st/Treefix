# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image = array_ops.placeholder(dtypes.float32, shape=pre_shape)
y = image_ops.resize_image_with_pad_v1(image, height, width)
self.assertEqual(y.get_shape().as_list(), post_shape)
