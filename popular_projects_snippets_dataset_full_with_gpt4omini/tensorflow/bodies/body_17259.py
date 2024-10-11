# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Read a cmyk jpeg image, and verify its shape.
path = ("tensorflow/core/lib/jpeg/testdata/"
        "jpeg_merge_test1_cmyk.jpg")
with self.cached_session():
    jpeg = io_ops.read_file(path)
    image_shape = self.evaluate(image_ops.extract_jpeg_shape(jpeg))
    # Cmyk jpeg image has 4 channels.
    self.assertAllEqual(image_shape, [256, 128, 4])
