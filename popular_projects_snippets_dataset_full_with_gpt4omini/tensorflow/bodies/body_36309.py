# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
nums = np.array([1, 2, 3, 4, 5, 6])
r = map_fn.map_fn(
    lambda x: x[0] * x[1][0] + x[1][1], (nums, (nums, -nums)),
    dtype=dtypes.int64)
self.assertEqual((6,), r.get_shape())
received = self.evaluate(r)
self.assertAllEqual(nums * nums + (-nums), received)
