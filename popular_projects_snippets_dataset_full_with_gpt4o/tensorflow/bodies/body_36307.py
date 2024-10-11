# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
nums = np.array([1, 2, 3, 4, 5, 6])
r = map_fn.map_fn(
    lambda x: ((x + 3) * 2, -(x + 3) * 2),
    nums,
    dtype=(dtypes.int64, dtypes.int64))
self.assertEqual(2, len(r))
self.assertEqual((6,), r[0].get_shape())
self.assertEqual((6,), r[1].get_shape())
received = self.evaluate(r)
self.assertAllEqual((nums + 3) * 2, received[0])
self.assertAllEqual(-(nums + 3) * 2, received[1])
