# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
v1 = variables.VariableAggregation
v2 = variables.VariableAggregationV2

self.assertEqual(v1.NONE, v2.NONE)
self.assertEqual(v1.SUM, v2.SUM)
self.assertEqual(v1.MEAN, v2.MEAN)
self.assertEqual(v1.ONLY_FIRST_REPLICA, v2.ONLY_FIRST_REPLICA)
self.assertEqual(v1.ONLY_FIRST_TOWER, v2.ONLY_FIRST_REPLICA)

self.assertEqual(v2.NONE, v1.NONE)
self.assertEqual(v2.SUM, v1.SUM)
self.assertEqual(v2.MEAN, v1.MEAN)
self.assertEqual(v2.ONLY_FIRST_REPLICA, v1.ONLY_FIRST_REPLICA)
self.assertEqual(v2.ONLY_FIRST_REPLICA, v1.ONLY_FIRST_TOWER)

self.assertEqual(hash(v1.NONE), hash(v2.NONE))
self.assertEqual(hash(v1.SUM), hash(v2.SUM))
self.assertEqual(hash(v1.MEAN), hash(v2.MEAN))
self.assertEqual(hash(v1.ONLY_FIRST_REPLICA), hash(v2.ONLY_FIRST_REPLICA))
self.assertEqual(hash(v1.ONLY_FIRST_TOWER), hash(v2.ONLY_FIRST_REPLICA))
