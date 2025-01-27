# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test if image_ops.adjust_jpeg_quality works when jpeq quality
# is an int (not tensor) for backward compatibility.
with ops.Graph().as_default(), self.test_session():
    np.random.seed(7)
    jpeg_quality = np.random.randint(40, 100)
    path = ("tensorflow/core/lib/jpeg/testdata/medium.jpg")
    jpeg = io_ops.read_file(path)
    image = image_ops.decode_jpeg(jpeg)
    adjust_jpeg_quality_image = image_ops.adjust_jpeg_quality(
        image, jpeg_quality)
    with self.cached_session() as sess:
        sess.run(adjust_jpeg_quality_image)
