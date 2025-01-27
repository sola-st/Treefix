# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, _ = self._get_test_object(
    None, None, num_gpus=required_gpus, use_devices_arg=use_devices_arg)
dataset_fn = lambda: dataset_ops.Dataset.range(10)
expected_values = [[i, i + 1] for i in range(0, 10, 2)]
input_fn = self._input_fn_to_test_input_context(
    dataset_fn,
    expected_num_replicas_in_sync=required_gpus,
    expected_num_input_pipelines=1,
    expected_input_pipeline_id=0)
self._test_input_fn_iterable(strategy, input_fn, expected_values)
