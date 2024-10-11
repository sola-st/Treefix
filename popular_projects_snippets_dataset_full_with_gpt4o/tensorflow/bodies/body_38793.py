# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_image_op_test.py
# Read some real PNGs, converting to different channel numbers
inputs = [(1, "lena_gray.png")]
for channels_in, filename in inputs:
    for channels in 0, 1, 3, 4:
        with self.cached_session() as sess:
            path = os.path.join(prefix_path, "png", "testdata", filename)
            png0 = io_ops.read_file(path)
            image0 = image_ops.decode_image(png0, channels=channels)
            image1 = image_ops.decode_png(png0, channels=channels)
            png0, image0, image1 = self.evaluate([png0, image0, image1])
            self.assertEqual(image0.shape, (26, 51, channels or channels_in))
            self.assertAllEqual(image0, image1)
