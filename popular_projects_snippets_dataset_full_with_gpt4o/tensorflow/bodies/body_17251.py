# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Confirm that CMYK reads in as RGB
base = "tensorflow/core/lib/jpeg/testdata"
rgb_path = os.path.join(base, "jpeg_merge_test1.jpg")
cmyk_path = os.path.join(base, "jpeg_merge_test1_cmyk.jpg")
shape = 256, 128, 3
for channels in 3, 0:
    with self.cached_session():
        rgb = image_ops.decode_jpeg(
            io_ops.read_file(rgb_path), channels=channels)
        cmyk = image_ops.decode_jpeg(
            io_ops.read_file(cmyk_path), channels=channels)
        rgb, cmyk = self.evaluate([rgb, cmyk])
        self.assertEqual(rgb.shape, shape)
        self.assertEqual(cmyk.shape, shape)
        error = self.averageError(rgb, cmyk)
        self.assertLess(error, 4)
