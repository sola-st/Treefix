# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Read a real jpeg and verify shape
path = ("tensorflow/core/lib/jpeg/testdata/"
        "jpeg_merge_test1.jpg")
with self.cached_session():
    jpeg0 = io_ops.read_file(path)
    image0 = image_ops.decode_jpeg(jpeg0)
    image1 = image_ops.decode_jpeg(image_ops.encode_jpeg(image0))
    jpeg0, image0, image1 = self.evaluate([jpeg0, image0, image1])
    self.assertEqual(len(jpeg0), 3771)
    self.assertEqual(image0.shape, (256, 128, 3))
    self.assertLess(self.averageError(image0, image1), 1.4)
