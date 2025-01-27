# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.session():
    with self.assertRaises(errors.InvalidArgumentError):
        x = np.ones((5, 1, 1, 2))
        v = image_ops.resize_images_v2(x, [1610637938, 1610637938],
                                       image_ops.ResizeMethod.BILINEAR)
        _ = self.evaluate(v)
