# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    # Encode it, then decode it, then encode it
    image0 = constant_op.constant(simple_color_ramp())
    jpeg0 = image_ops.encode_jpeg(image0)
    image1 = image_ops.decode_jpeg(jpeg0, dct_method="INTEGER_ACCURATE")
    image2 = image_ops.decode_jpeg(
        image_ops.encode_jpeg(image1), dct_method="INTEGER_ACCURATE")
    jpeg0, image0, image1, image2 = self.evaluate(
        [jpeg0, image0, image1, image2])

    # The decoded-encoded image should be similar to the input
    self.assertLess(self.averageError(image0, image1), 0.6)

    # We should be very close to a fixpoint
    self.assertLess(self.averageError(image1, image2), 0.02)

    # Smooth ramps compress well (input size is 153600)
    self.assertGreaterEqual(len(jpeg0), 5000)
    self.assertLessEqual(len(jpeg0), 6000)
