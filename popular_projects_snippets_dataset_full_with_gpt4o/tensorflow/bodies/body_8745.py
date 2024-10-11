# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
dataset_fn = lambda: dataset_ops.Dataset.range(100)
num_gpus = self._get_num_gpus()  # pylint: disable=assignment-from-no-return
num_workers = 1

expected_values = [[i+j for j in range(num_gpus)] * num_workers
                   for i in range(0, 100, num_gpus)]

# Dummy cached_session is used in Eager
with self.cached_session() as sess:
    # `expected_input_pipeline_id` is None because the input_fn will be called
    # multiple times, each with a different input_pipeline_id.
    input_fn = self._input_fn_to_test_input_context(
        dataset_fn,
        expected_num_replicas_in_sync=num_workers*num_gpus,
        expected_num_input_pipelines=num_workers,
        expected_input_pipeline_id=None)
    iterator = distribution.make_input_fn_iterator(input_fn)
    self._test_input_fn_iterator(
        iterator, distribution.extended.worker_devices, expected_values, sess)
