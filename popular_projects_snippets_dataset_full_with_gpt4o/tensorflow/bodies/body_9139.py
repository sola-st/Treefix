# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
self.assertEqual(cluster_spec.as_dict(), cs)
self.assertEqual(task_type, "ps")
self.assertEqual(task_id, 0)
self.assertEqual(session_config.experimental.collective_group_leader,
                 "/job:worker/replica:0/task:0")
self.assertEqual(session_config.intra_op_parallelism_threads, 1)
self.assertEqual(rpc_layer, "grpc")

exit(MockServer())
