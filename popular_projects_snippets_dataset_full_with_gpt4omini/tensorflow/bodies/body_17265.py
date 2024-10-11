# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    # Encode it, then decode it
    image0 = constant_op.constant(simple_color_ramp())
    png0 = image_ops.encode_png(image0, compression=7)
    image1 = image_ops.decode_png(png0)
    png0, image0, image1 = self.evaluate([png0, image0, image1])

    # PNG is lossless
    self.assertAllEqual(image0, image1)

    # Smooth ramps compress well, but not too well
    self.assertGreaterEqual(len(png0), 400)
    self.assertLessEqual(len(png0), 1150)
