# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = image_ops_impl.crop_and_resize_v2(
            image=np.ones((1, 1, 1, 1)),
            boxes=np.ones((11, 4)),
            box_indices=np.ones((11)),
            crop_size=[2065374891, 1145309325])
        self.evaluate(op)
