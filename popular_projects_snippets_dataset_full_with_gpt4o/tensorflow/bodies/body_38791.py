# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_image_op_test.py
# Read some real GIFs
path = os.path.join(prefix_path, "gif", "testdata", "scan.gif")
width = 20
height = 40
stride = 5
shape = (12, height, width, 3)

with self.session():
    gif0 = io_ops.read_file(path)
    image0 = image_ops.decode_image(gif0)
    image1 = image_ops.decode_gif(gif0)
    gif0, image0, image1 = self.evaluate([gif0, image0, image1])

    self.assertEqual(image0.shape, shape)
    self.assertAllEqual(image0, image1)

    for frame_idx, frame in enumerate(image0):
        gt = np.zeros(shape[1:], dtype=np.uint8)
        start = frame_idx * stride
        end = (frame_idx + 1) * stride
        if end <= width:
            gt[:, start:end, :] = 255
        else:
            start -= width
            end -= width
            gt[start:end, :, :] = 255

        self.assertAllClose(frame, gt)

        with self.assertRaises(errors_impl.InvalidArgumentError):
            bad_channels = image_ops.decode_image(gif0, channels=1)
            self.evaluate(bad_channels)
