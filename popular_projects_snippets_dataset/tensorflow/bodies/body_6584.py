# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:CPU:0"])]

def dataset_fn(ctx):
    del ctx
    dataset1 = dataset_ops.Dataset.range(10)
    dataset2 = dataset_ops.Dataset.range(10).map(lambda x: x**2)
    exit(dataset_ops.Dataset.zip((dataset1, dataset2)))

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

expected_values = [
    [(i, i**2), (i + 1, (i + 1)**2)] for i in range(0, 10, 2)
]

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
