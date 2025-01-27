# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test if all frames in the animated GIF file is properly decoded.
with self.cached_session():
    base = "tensorflow/core/lib/gif/testdata"
    gif = io_ops.read_file(os.path.join(base, "pendulum_sm.gif"))
    gt_frame0 = io_ops.read_file(os.path.join(base, "pendulum_sm_frame0.png"))
    gt_frame1 = io_ops.read_file(os.path.join(base, "pendulum_sm_frame1.png"))
    gt_frame2 = io_ops.read_file(os.path.join(base, "pendulum_sm_frame2.png"))

    image = image_ops.decode_gif(gif)
    frame0 = image_ops.decode_png(gt_frame0)
    frame1 = image_ops.decode_png(gt_frame1)
    frame2 = image_ops.decode_png(gt_frame2)
    image, frame0, frame1, frame2 = self.evaluate([image, frame0, frame1,
                                                   frame2])
    # Compare decoded gif frames with ground-truth data.
    self.assertAllEqual(image[0], frame0)
    self.assertAllEqual(image[1], frame1)
    self.assertAllEqual(image[2], frame2)
