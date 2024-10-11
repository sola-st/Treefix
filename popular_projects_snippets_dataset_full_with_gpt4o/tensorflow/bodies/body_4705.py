# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
input_context = distribute_lib.InputContext(
    num_input_pipelines=2, input_pipeline_id=1, num_replicas_in_sync=6)
self.assertEqual(6, input_context.num_replicas_in_sync)
self.assertEqual(1, input_context.input_pipeline_id)
self.assertEqual(2, input_context.num_input_pipelines)
