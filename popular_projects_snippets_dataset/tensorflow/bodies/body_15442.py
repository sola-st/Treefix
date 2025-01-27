# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
resize = image_ops.resize_images if v1 else image_ops.resize_images_v2

# Construct the input images.
channels = 3
images = self.make_image_batch(src_sizes, channels)
expected_shape = [len(src_sizes)] + list(dst_size) + [channels]

# Resize the ragged batch of images.
resized_images = resize(images, dst_size)
self.assertIsInstance(resized_images, ops.Tensor)
self.assertEqual(resized_images.shape.as_list(), expected_shape)

# Check that results for each image matches what we'd get with the
# non-batch version of tf.images.resize.
for i in range(len(src_sizes)):
    actual = resized_images[i]
    expected = resize(images[i].to_tensor(), dst_size)
    self.assertAllClose(actual, expected)
