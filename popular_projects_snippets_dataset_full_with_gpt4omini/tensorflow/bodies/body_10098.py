# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.float32, np.double]:
    x = dtype(1)
    y = dtype(1.00009)
    z = False
    with test_util.device(use_gpu=True):
        # Default tolerance is 0.00001
        z_tf = self.evaluate(math_ops.approximate_equal(x, y))
        self.assertAllEqual(z, z_tf)

for dtype in [np.float32, np.double]:
    x = dtype(1)
    y = dtype(1.000009)
    z = True
    with test_util.device(use_gpu=True):
        # Default tolerance is 0.00001
        z_tf = self.evaluate(math_ops.approximate_equal(x, y))
        self.assertAllEqual(z, z_tf)

for dtype in [np.float32, np.double]:
    x = np.array([[[[-1, 2.00009999], [-3, 4.01]]]], dtype=dtype)
    y = np.array([[[[-1.001, 2], [-3.00009, 4]]]], dtype=dtype)
    z = np.array([[[[False, True], [True, False]]]], dtype=np.bool_)
    with test_util.device(use_gpu=True):
        z_tf = self.evaluate(math_ops.approximate_equal(x, y, tolerance=0.0001))
        self.assertAllEqual(z, z_tf)
