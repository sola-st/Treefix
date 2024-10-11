# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
# Use a list of one element as counter so that it can be captured by the
# `_input_fn`. This counter is incremented by 1 each time an input_fn is
# called. We use this counter to check whether the `input_pipeline_id`
# matches the counter in the in-graph replication.
worker_id_counter = [0]

def _input_fn(input_context):
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

exit(_input_fn)
