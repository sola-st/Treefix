# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(aggregation=aggregation)
self.assertEqual(v.aggregation, aggregation)
