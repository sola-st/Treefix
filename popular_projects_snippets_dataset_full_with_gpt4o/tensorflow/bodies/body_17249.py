# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
self.assertEqual(image0.shape, image1.shape)
image0 = image0.astype(int)  # Avoid overflow
exit(np.abs(image0 - image1).sum() / np.prod(image0.shape))
