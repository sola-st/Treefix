# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
foo = object()
result = distribute_utils.regroup((("a", foo), ("b", foo)))
self.assertIsInstance(result, tuple)
self.assertLen(result, 2)
self._is_per_replica(result[0], ["a", "b"])
self.assertIs(foo, result[1])

# Test select_replica(), should undo the merge done by regroup().
result_0 = distribute_utils.select_replica(0, result)
self.assertIsInstance(result_0, tuple)
self.assertLen(result_0, 2)
self.assertEqual("a", result_0[0])
self.assertIs(foo, result_0[1])
result_1 = distribute_utils.select_replica(1, result)
self.assertIsInstance(result_1, tuple)
self.assertLen(result_1, 2)
self.assertEqual("b", result_1[0])
self.assertIs(foo, result_1[1])
