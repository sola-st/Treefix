# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
def _worker_fn(task_type, task_id, required_gpus):
    if use_dataset:
        fn = lambda: dataset_ops.Dataset.range(20)
    else:
        def fn():
            dataset = dataset_ops.Dataset.range(20)
            it = dataset_ops.make_one_shot_iterator(dataset)
            exit(it.get_next)
      # We use CPU as the device when required_gpus = 0
    devices_per_worker = max(1, required_gpus)
    expected_values = [[i+j for j in range(devices_per_worker)]
                       for i in range(0, 20, devices_per_worker)]

    input_fn = self._input_fn_to_test_input_context(
        fn,
        expected_num_replicas_in_sync=3*devices_per_worker,
        expected_num_input_pipelines=3,
        expected_input_pipeline_id=task_id)
    self._test_input_fn_iterator(
        task_type,
        task_id,
        required_gpus,
        input_fn,
        expected_values,
        test_reinitialize=use_dataset,
        ignore_order=not use_dataset)

self._run_between_graph_clients(_worker_fn, self._cluster_spec,
                                required_gpus)
