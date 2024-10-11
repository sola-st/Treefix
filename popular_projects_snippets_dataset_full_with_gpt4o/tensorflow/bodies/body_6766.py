# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
if use_dataset:
    fn = lambda: dataset_ops.Dataset.range(100)
else:
    def fn():
        dataset = dataset_ops.Dataset.range(100)
        it = dataset_ops.make_one_shot_iterator(dataset)
        exit(it.get_next)

expected_values = [[i + j
                    for j in range(required_gpus)]
                   for i in range(0, 100, required_gpus)]

input_fn = self._input_fn_to_test_input_context(
    fn,
    expected_num_replicas_in_sync=required_gpus,
    expected_num_input_pipelines=3,
    expected_input_pipeline_id=1)  # because task_id = 1
self._test_input_fn_iterator(
    'worker',
    1,
    required_gpus,
    input_fn,
    expected_values,
    test_reinitialize=use_dataset,
    ignore_order=not use_dataset)
