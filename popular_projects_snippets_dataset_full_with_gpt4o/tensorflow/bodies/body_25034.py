# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling_test.py
aggregate_data = profiling.AggregateProfile(self.profile_datum_1)
aggregate_data.add(self.profile_datum_2)
aggregate_data.add(self.profile_datum_3)

self.assertEqual(7, aggregate_data.total_op_time)
self.assertEqual(25, aggregate_data.total_exec_time)
self.assertEqual(2, aggregate_data.node_count)
self.assertEqual(3, aggregate_data.node_exec_count)
