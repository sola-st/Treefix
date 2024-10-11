# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_image_op_test.py
# Read a real bmp and verify shape
path = os.path.join(prefix_path, "bmp", "testdata", "lena.bmp")
with self.session():
    bmp0 = io_ops.read_file(path)
    image0 = image_ops.decode_image(bmp0)
    image1 = image_ops.decode_bmp(bmp0)
    bmp0, image0, image1 = self.evaluate([bmp0, image0, image1])
    self.assertEqual(len(bmp0), 4194)
    self.assertAllEqual(image0, image1)
