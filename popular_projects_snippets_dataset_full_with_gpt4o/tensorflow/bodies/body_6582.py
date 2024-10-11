# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = collections.OrderedDict()
for tpu_device in distribution.extended.worker_devices:
    host_device = device_util.get_host_for_device(tpu_device)
    worker_device_pairs.setdefault(host_device, [])
    worker_device_pairs[host_device].append(tpu_device)
worker_device_pairs = worker_device_pairs.items()
dataset_fn = lambda _: dataset_ops.Dataset.range(10)
dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

expected_values = [[i, i + 1] for i in range(0, 10, 2)]

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
