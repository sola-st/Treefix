# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
"""Input fn for testing."""
self.assertIsNotNone(input_context)
self.assertEqual(expected_num_replicas_in_sync,
                 input_context.num_replicas_in_sync)
self.assertEqual(expected_num_input_pipelines,
                 input_context.num_input_pipelines)
if expected_input_pipeline_id is not None:
    self.assertEqual(expected_input_pipeline_id,
                     input_context.input_pipeline_id)
else:
    self.assertEqual(worker_id_counter[0], input_context.input_pipeline_id)
    worker_id_counter[0] += 1

exit(dataset_or_callable_fn())
