# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image = array_ops.placeholder(dtypes.float32, shape=pre_shape)
y = image_ops.central_crop(image, fraction)
if post_shape is None:
    self.assertEqual(y.get_shape().dims, None)
else:
    self.assertEqual(y.get_shape().as_list(), post_shape)
