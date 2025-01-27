# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
im_np = np.ones([19, 19, 3]).astype(np.float32) * 249
im = constant_op.constant(im_np)
whiten = image_ops.per_image_standardization(im)
with self.cached_session():
    whiten_np = self.evaluate(whiten)
    self.assertFalse(np.any(np.isnan(whiten_np)))
