# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Previous implementation of random_jpeg_quality had a bug.
# This unit test tests the fixed version, but due to forward compatibility
# this test can only be done when fixed version is used.
# Test jpeg quality dynamic randomization.
with ops.Graph().as_default(), self.test_session():
    np.random.seed(7)
    path = ("tensorflow/core/lib/jpeg/testdata/medium.jpg")
    jpeg = io_ops.read_file(path)
    image = image_ops.decode_jpeg(jpeg)
    random_jpeg_image = image_ops.random_jpeg_quality(image, 40, 100)
    with self.cached_session() as sess:
        # Test randomization.
        random_jpeg_images = [sess.run(random_jpeg_image) for _ in range(5)]
        are_images_equal = []
        for i in range(1, len(random_jpeg_images)):
            # Most of them should be different if randomization is occurring
            # correctly.
            are_images_equal.append(
                np.array_equal(random_jpeg_images[0], random_jpeg_images[i]))
        self.assertFalse(all(are_images_equal))
