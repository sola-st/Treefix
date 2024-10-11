# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_image_op_test.py
# Read a real jpeg and verify shape
path = os.path.join(prefix_path, "jpeg", "testdata", "jpeg_merge_test1.jpg")
with self.session():
    jpeg0 = io_ops.read_file(path)
    image0 = image_ops.decode_image(jpeg0)
    image1 = image_ops.decode_jpeg(jpeg0)
    jpeg0, image0, image1 = self.evaluate([jpeg0, image0, image1])
    self.assertEqual(len(jpeg0), 3771)
    self.assertEqual(image0.shape, (256, 128, 3))
    self.assertAllEqual(image0, image1)

    with self.assertRaises(errors_impl.InvalidArgumentError):
        bad_channels = image_ops.decode_image(jpeg0, channels=4)
        self.evaluate(bad_channels)
