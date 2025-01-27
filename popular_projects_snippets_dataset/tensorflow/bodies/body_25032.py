# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling_test.py
aggregate_data = profiling.AggregateProfile(self.profile_datum_1)

self.assertEqual(2, aggregate_data.total_op_time)
self.assertEqual(4, aggregate_data.total_exec_time)
self.assertEqual(1, aggregate_data.node_count)
self.assertEqual(1, aggregate_data.node_exec_count)
