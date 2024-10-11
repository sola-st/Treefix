# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session() as sess:
    # Encode it, then decode it, then encode it
    base = "tensorflow/core/lib/jpeg/testdata"
    jpeg0 = io_ops.read_file(os.path.join(base, "jpeg_merge_test1.jpg"))

    h, w, _ = 256, 128, 3
    # Invalid crop windows.
    crop_windows = [[-1, 11, 11, 11], [11, -1, 11, 11], [11, 11, -1, 11],
                    [11, 11, 11, -1], [11, 11, 0, 11], [11, 11, 11, 0],
                    [0, 0, h + 1, w], [0, 0, h, w + 1]]
    for crop_window in crop_windows:
        with self.assertRaisesRegex(
            (ValueError, errors.InvalidArgumentError),
            "Invalid JPEG data or crop window"):
            result = image_ops.decode_and_crop_jpeg(jpeg0, crop_window)
            self.evaluate(result)
