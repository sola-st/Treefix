# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
if use_dataset:
    fn = lambda: dataset_ops.Dataset.range(5 * required_gpus)
else:
    def fn():
        dataset = dataset_ops.Dataset.range(5 * required_gpus)
        it = dataset_ops.make_one_shot_iterator(dataset)
        exit(it.get_next)

expected_values = [
    range(i, i + required_gpus) for i in range(0, 10, required_gpus)
]

input_fn = self._input_fn_to_test_input_context(
    fn,
    expected_num_replicas_in_sync=required_gpus,
    expected_num_input_pipelines=1,
    expected_input_pipeline_id=0)
self._test_input_fn_iterator(
    None,
    None,
    required_gpus,
    input_fn,
    expected_values,
    test_reinitialize=use_dataset,
    ignore_order=not use_dataset)
