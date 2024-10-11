# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Read some real PNGs, converting to different channel numbers
prefix = "tensorflow/core/lib/png/testdata/"
inputs = ((1, "lena_gray.png"), (4, "lena_rgba.png"),
          (3, "lena_palette.png"), (4, "lena_palette_trns.png"))
for channels_in, filename in inputs:
    for channels in 0, 1, 3, 4:
        with self.cached_session():
            png0 = io_ops.read_file(prefix + filename)
            image0 = image_ops.decode_png(png0, channels=channels)
            png0, image0 = self.evaluate([png0, image0])
            self.assertEqual(image0.shape, (26, 51, channels or channels_in))
            if channels == channels_in:
                image1 = image_ops.decode_png(image_ops.encode_png(image0))
                self.assertAllEqual(image0, self.evaluate(image1))
