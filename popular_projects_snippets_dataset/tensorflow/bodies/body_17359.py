# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            "must be rank 1"):
    op = image_ops_impl.crop_and_resize_v2(
        image=np.ones((2, 2, 2, 2)),
        boxes=np.ones((0, 4)),
        box_indices=np.ones((0, 1)),
        crop_size=[1, 1])
    self.evaluate(op)
