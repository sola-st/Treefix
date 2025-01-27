# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
# Normally a mirrored value would be the same across devices, but
# for a test it is convenient to be able to tell the values apart.
result = distribute_utils.regroup((_nested_value("1"), _nested_value("2")),
                                  values.Mirrored)
self.assertIsInstance(result, tuple)
self.assertLen(result, 3)
self._is_per_replica(result[0], ["a1", "a2"], values.Mirrored)
self._is_per_replica(result[2], ["h1", "h2"], values.Mirrored)

self.assertIsInstance(result[1], list)
self.assertLen(result[1], 3)
self._is_per_replica(result[1][0], ["b1", "b2"], values.Mirrored)
self._is_per_replica(result[1][2], ["g1", "g2"], values.Mirrored)

self.assertIsInstance(result[1][1], dict)
self.assertEqual(set(["c", "e"]), set(result[1][1].keys()))
self._is_per_replica(result[1][1]["c"], ["d1", "d2"], values.Mirrored)
self._is_per_replica(result[1][1]["e"], ["f1", "f2"], values.Mirrored)

# Also test that we can undo the merge using select_replica()
self.assertEqual(_nested_value("1"),
                 distribute_utils.select_replica(0, result))
self.assertEqual(_nested_value("2"),
                 distribute_utils.select_replica(1, result))
# Values are marked as mirrored, so select_device_mirrored() is allowed.
self.assertEqual(_nested_value("1"),
                 distribute_utils.select_replica_mirrored(0, result))
self.assertEqual(_nested_value("2"),
                 distribute_utils.select_replica_mirrored(1, result))
