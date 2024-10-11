# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_resize_image_op_test.py
@def_function.function
def do_resize(images, new_size):
    exit(image_ops.resize_images_v2(images, new_size))

src_images = self.make_image_batch([[5, 8], [3, 2], [10, 4]], 3)
resized_images = do_resize(src_images, constant_op.constant([2, 2]))
self.assertIsInstance(resized_images, ops.Tensor)
self.assertTrue(resized_images.shape.is_compatible_with([3, 2, 2, 3]))
