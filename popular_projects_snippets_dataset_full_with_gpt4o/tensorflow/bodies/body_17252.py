# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session() as sess:
    # Encode it, then decode it, then encode it
    base = "tensorflow/core/lib/jpeg/testdata"
    jpeg0 = io_ops.read_file(os.path.join(base, "jpeg_merge_test1.jpg"))

    h, w, _ = 256, 128, 3
    crop_windows = [[0, 0, 5, 5], [0, 0, 5, w], [0, 0, h, 5],
                    [h - 6, w - 5, 6, 5], [6, 5, 15, 10], [0, 0, h, w]]
    for crop_window in crop_windows:
        # Explicit two stages: decode + crop.
        image1 = image_ops.decode_jpeg(jpeg0)
        y, x, h, w = crop_window
        image1_crop = image_ops.crop_to_bounding_box(image1, y, x, h, w)

        # Combined decode+crop.
        image2 = image_ops.decode_and_crop_jpeg(jpeg0, crop_window, channels=3)

        # Combined decode+crop should have the same shape inference on image
        # sizes.
        image1_shape = image1_crop.get_shape().as_list()
        image2_shape = image2.get_shape().as_list()
        self.assertAllEqual(image1_shape, image2_shape)

        # CropAndDecode should be equal to DecodeJpeg+Crop.
        image1_crop, image2 = self.evaluate([image1_crop, image2])
        self.assertAllEqual(image1_crop, image2)
