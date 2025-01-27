# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
imgs_np = np.random.uniform(0., 255., [4, 24, 24, 3])
whiten_np = [self._NumpyPerImageWhitening(img) for img in imgs_np]
with self.cached_session():
    imgs = constant_op.constant(imgs_np)
    whiten = image_ops.per_image_standardization(imgs)
    whiten_tf = self.evaluate(whiten)
    for w_tf, w_np in zip(whiten_tf, whiten_np):
        self.assertAllClose(w_tf, w_np, atol=1e-4)
