# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
npt = np.arange(1, 19, dtype=np.float32).reshape(3, 2, 3)
t = constant_op.constant(npt)

self.assertAllEqual(npt[:, :, :], t[:, :, :])
self.assertAllEqual(npt[::, ::, ::], t[::, ::, ::])
self.assertAllEqual(npt[::1, ::1, ::1], t[::1, ::1, ::1])
self.assertAllEqual(npt[::1, ::5, ::2], t[::1, ::5, ::2])
self.assertAllEqual(npt[::-1, :, :], t[::-1, :, :])
self.assertAllEqual(npt[:, ::-1, :], t[:, ::-1, :])
self.assertAllEqual(npt[:, :, ::-1], t[:, :, ::-1])
self.assertAllEqual(npt[-2::-1, :, ::1], t[-2::-1, :, ::1])
self.assertAllEqual(npt[-2::-1, :, ::2], t[-2::-1, :, ::2])
