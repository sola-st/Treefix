# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    # Compare decoding with both dct_option=INTEGER_FAST and
    # default.  They should be the same.
    image0 = constant_op.constant(simple_color_ramp())
    jpeg0 = image_ops.encode_jpeg(image0)
    image1 = image_ops.decode_jpeg(jpeg0, dct_method="INTEGER_FAST")
    image2 = image_ops.decode_jpeg(jpeg0)
    image1, image2 = self.evaluate([image1, image2])

    # The images should be the same.
    self.assertAllClose(image1, image2)
