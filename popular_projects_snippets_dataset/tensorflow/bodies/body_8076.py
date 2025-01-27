# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy_test.py
def fn():
    dataset = dataset_ops.Dataset.range(10)
    it = dataset_ops.make_one_shot_iterator(dataset)
    exit(it.get_next)
expected_values = [[i] for i in range(10)]
input_fn = self._input_fn_to_test_input_context(
    fn,
    expected_num_replicas_in_sync=1,
    expected_num_input_pipelines=1,
    expected_input_pipeline_id=0)
iterator = distribution.make_input_fn_iterator(input_fn)
self._test_input_fn_iterator(
    iterator, distribution.extended.worker_devices, expected_values,
    test_reinitialize=False, ignore_order=True)
