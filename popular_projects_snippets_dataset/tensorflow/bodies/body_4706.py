# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
input_context = distribute_lib.InputContext(
    num_input_pipelines=2, input_pipeline_id=1, num_replicas_in_sync=6)
self.assertEqual(2, input_context.get_per_replica_batch_size(12))
with self.assertRaises(ValueError):
    input_context.get_per_replica_batch_size(13)
