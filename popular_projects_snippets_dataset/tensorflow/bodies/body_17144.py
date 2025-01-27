# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image = array_ops.placeholder(dtypes.float32, shape=pre_shape)
y = image_ops.pad_to_bounding_box_internal(
    image, 0, 0, height, width, check_dims=False)
self.assertEqual(y.get_shape().as_list(), post_shape)
