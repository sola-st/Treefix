# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    # Strip the b channel from an rgb image to get a two-channel image.
    gray_alpha = simple_color_ramp()[:, :, 0:2]
    image0 = constant_op.constant(gray_alpha)
    png0 = image_ops.encode_png(image0, compression=7)
    image1 = image_ops.decode_png(png0)
    png0, image0, image1 = self.evaluate([png0, image0, image1])
    self.assertEqual(2, image0.shape[-1])
    self.assertAllEqual(image0, image1)
