# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:CPU:0"])]
batch_size = 10
dataset_fn = lambda _: dataset_ops.Dataset.range(100).batch(batch_size)
dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

updated_batch_size = (
    batch_size //
    num_replicas_in_sync if num_replicas_in_sync else batch_size)
expected_values = [[
    range(i, i + updated_batch_size),
    range(i + updated_batch_size, i + 2 * updated_batch_size)
] for i in range(0, 100, updated_batch_size * 2)]

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
self._test_input_iteration(
    input_type,
    api_type,
    iteration_type,
    dataset_or_input_fn,
    worker_device_pairs,
    expected_values,
    distribution,
    sess=None,
    num_replicas_in_sync=num_replicas_in_sync)
