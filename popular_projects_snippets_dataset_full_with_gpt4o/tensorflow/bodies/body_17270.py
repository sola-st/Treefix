# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Read some real GIFs
prefix = "tensorflow/core/lib/gif/testdata/"
WIDTH = 20
HEIGHT = 40
STRIDE = 5
shape = (12, HEIGHT, WIDTH, 3)

with self.cached_session():
    gif0 = io_ops.read_file(prefix + filename)
    image0 = image_ops.decode_gif(gif0)
    gif0, image0 = self.evaluate([gif0, image0])

    self.assertEqual(image0.shape, shape)

    for frame_idx, frame in enumerate(image0):
        gt = np.zeros(shape[1:], dtype=np.uint8)
        start = frame_idx * STRIDE
        end = (frame_idx + 1) * STRIDE
        print(frame_idx)
        if end <= WIDTH:
            gt[:, start:end, :] = 255
        else:
            start -= WIDTH
            end -= WIDTH
            gt[start:end, :, :] = 255

        self.assertAllClose(frame, gt)
