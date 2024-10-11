# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:CPU:0"])]
dataset_fn = lambda _: dataset_ops.Dataset.range(9).batch(  # pylint: disable=g-long-lambda
    2, drop_remainder=drop_remainder)
dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)

# The last global batch only contains data for one replica.
if drop_remainder:
    expected_values = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
else:
    expected_values = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8], []]]
distribution.extended.experimental_enable_get_next_as_optional = True
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
