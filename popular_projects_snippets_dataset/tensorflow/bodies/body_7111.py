# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if tf2.enabled() and not context.executing_eagerly():
    self.skipTest("Skipping test since we do not support graph mode in TF 2")

dataset_fn = lambda: dataset_ops.Dataset.range(10)
expected_values = [[i, i+1] for i in range(0, 10, 2)]
input_fn = self._input_fn_to_test_input_context(
    dataset_fn,
    expected_num_replicas_in_sync=2,
    expected_num_input_pipelines=1,
    expected_input_pipeline_id=0)
self._test_input_fn_iterable(distribution, input_fn, expected_values)
