# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
result = distribute_utils.regroup((_nested_value("1"),))
# On one device regroup() and select_replica() are basically identity.
self.assertEqual(_nested_value("1"), result)
self.assertEqual(_nested_value("1"),
                 distribute_utils.select_replica(0, result))
