# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Read a real jpeg and verify shape.
path = ("tensorflow/core/lib/jpeg/testdata/"
        "jpeg_merge_test1.jpg")
with self.cached_session():
    jpeg = io_ops.read_file(path)
    # Extract shape without decoding.
    image_shape = self.evaluate(image_ops.extract_jpeg_shape(jpeg))
    self.assertAllEqual(image_shape, [256, 128, 3])
