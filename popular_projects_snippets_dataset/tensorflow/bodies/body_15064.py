# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt1 = ragged_factory_ops.constant([[1, 2], [3, 4, 5], [6], [], [7]])
rt2 = ragged_factory_ops.constant([[[1, 2], [3, 4, 5]], [[6]], [], [[],
                                                                    [7]]])

rt1_plus_10 = rt1.with_values(rt1.values + 10)
rt2_times_10 = rt2.with_flat_values(rt2.flat_values * 10)
rt1_expanded = rt1.with_values(array_ops.expand_dims(rt1.values, axis=1))

self.assertAllEqual(rt1_plus_10, [[11, 12], [13, 14, 15], [16], [], [17]])
self.assertAllEqual(rt2_times_10,
                    [[[10, 20], [30, 40, 50]], [[60]], [], [[], [70]]])
self.assertAllEqual(rt1_expanded,
                    [[[1], [2]], [[3], [4], [5]], [[6]], [], [[7]]])
