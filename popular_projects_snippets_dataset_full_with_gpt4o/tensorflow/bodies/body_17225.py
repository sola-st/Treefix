# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = image_ops.resize_images_v2(
            images=np.ones((2, 2, 2, 2)),
            size=[1801181592, 1846789676],
            antialias=True)
        self.evaluate(op)
