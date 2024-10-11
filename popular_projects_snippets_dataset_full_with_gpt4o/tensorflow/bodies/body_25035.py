# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling_test.py
aggregate_data = profiling.AggregateProfile(self.profile_datum_1)
aggregate_data.add(self.profile_datum_4)

self.assertEqual(4, aggregate_data.total_op_time)
self.assertEqual(8, aggregate_data.total_exec_time)
self.assertEqual(2, aggregate_data.node_count)
self.assertEqual(2, aggregate_data.node_exec_count)
