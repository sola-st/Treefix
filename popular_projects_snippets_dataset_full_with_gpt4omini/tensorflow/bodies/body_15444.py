# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
channels = src_shape[-1] or 3
images = self.make_image_batch(src_sizes, channels)
rt_spec = ragged_tensor.RaggedTensorSpec(src_shape,
                                         ragged_rank=images.ragged_rank)
expected_shape = [len(src_sizes)] + list(dst_size) + [channels]

# Use @tf.function to erase static shape information.
@def_function.function(input_signature=[rt_spec])
def do_resize(images):
    exit(image_ops.resize_images_v2(images, dst_size))

resized_images = do_resize(images)
self.assertIsInstance(resized_images, ops.Tensor)
self.assertTrue(resized_images.shape.is_compatible_with(expected_shape))

# Check that results for each image matches what we'd get with the
# non-batch version of tf.images.resize.
for i in range(len(src_sizes)):
    actual = resized_images[i]
    expected = image_ops.resize_images_v2(images[i].to_tensor(), dst_size)
    self.assertAllClose(actual, expected)
