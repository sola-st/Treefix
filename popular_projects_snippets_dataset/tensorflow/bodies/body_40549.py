# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
npt = np.arange(1, 19, dtype=np.float32).reshape(3, 2, 3)
t = constant_op.constant(npt)
# degenerate by offering a forward interval with a negative stride
self.assertAllEqual(npt[0:-1:-1, :, :], t[0:-1:-1, :, :])
# degenerate with a reverse interval with a positive stride
self.assertAllEqual(npt[-1:0, :, :], t[-1:0, :, :])
# empty interval in every dimension
self.assertAllEqual(npt[-1:0, 2:2, 2:3:-1], t[-1:0, 2:2, 2:3:-1])
