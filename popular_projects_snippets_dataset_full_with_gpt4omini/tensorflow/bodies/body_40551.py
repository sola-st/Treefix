# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
npt = np.array([[[[[1, 2, 4, 5], [5, 6, 7, 8], [9, 10, 11, 12]]],
                 [[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]]])
t = constant_op.constant(npt)
self.assertAllEqual(npt[:, :, :, :, 3], t[:, :, :, :, 3])
self.assertAllEqual(npt[..., 3], t[..., 3])
self.assertAllEqual(npt[:, 0], t[:, 0])
self.assertAllEqual(npt[:, :, 0], t[:, :, 0])
