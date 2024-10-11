# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
result = distribute_utils.regroup([("1", "2"), ("3", "4")])
self.assertIsInstance(result, tuple)
self.assertLen(result, 2)
self._is_per_replica(result[0], ("1", "3"), values.PerReplica)
self._is_per_replica(result[1], ("2", "4"), values.PerReplica)
