# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
npt = np.array(
    [[[[[1, 2], [3, 4], [5, 6]]], [[[7, 8], [9, 10], [11, 12]]]]])
t = constant_op.constant(npt)

self.assertAllEqual(npt[0:], t[0:])
# implicit ellipsis
self.assertAllEqual(npt[0:, ...], t[0:, ...])
# ellipsis alone
self.assertAllEqual(npt[...], t[...])
# ellipsis at end
self.assertAllEqual(npt[0:1, ...], t[0:1, ...])
# ellipsis at begin
self.assertAllEqual(npt[..., 0:1], t[..., 0:1])
# ellipsis at middle
self.assertAllEqual(npt[0:1, ..., 0:1], t[0:1, ..., 0:1])
