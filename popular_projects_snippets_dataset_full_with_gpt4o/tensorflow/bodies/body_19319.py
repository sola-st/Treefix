# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
batch_size = 1
image_height = 10
image_width = 10
channels = 1
image_shape = (batch_size, image_height, image_width, channels)
num_boxes = 3
boxes_shape = (num_boxes, 4)
random_seed.set_seed(123)
image = random_ops.random_normal(shape=image_shape, dtype=dtype)
boxes = random_ops.random_uniform(shape=boxes_shape, dtype=dtypes.float32)
box_indices = random_ops.random_uniform(
    shape=(num_boxes,), minval=0, maxval=batch_size, dtype=dtypes.int32)
crop_size = constant_op.constant([3, 3], dtype=dtypes.int32)
exit((image, boxes, box_indices, crop_size))
