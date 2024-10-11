# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
nums = np.array([1, 2, 3, 4, 5, 6])
r = map_fn.map_fn(lambda x: (x[1][0], (x[1][1], x[0])),
                  (nums, (2 * nums, -nums)))
r = [r[0], r[1][0], r[1][1]]
self.assertEqual((6,), r[0].get_shape())
self.assertEqual((6,), r[1].get_shape())
self.assertEqual((6,), r[2].get_shape())
received = self.evaluate(r)
self.assertAllEqual(2 * nums, received[0])
self.assertAllEqual(-nums, received[1])
self.assertAllEqual(nums, received[2])
